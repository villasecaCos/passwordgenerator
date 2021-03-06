#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Represents the controller of the application. It forwards
information from the model to the view, and viceversa. It also creates the new
passwords.'''

import logging
from controller.password import Password
from view.main_frame import MainFrame
from model.file_manager import FileManager

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

FORMAT = '%(asctime)s:%(module)s:%(levelname)s:%(message)s'
formatter = logging.Formatter(FORMAT)

file_handler = logging.FileHandler('controller/controller.log', mode='w')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Relayer():
    """
    It coordinates the view and the model. Creates the new passwords.
    ...

    Attributes
    ----------
    file_manager : FileManager
        Instance of the model.
    keys : dict_keys
        keys of the underlying data model(a dictionary) of the model.
    main_frame : MainFrame
        Instance of the view.
    current_password: Password
        Instance of the password, actually, being displayed.
    final_set: set
        the set corresponding to the current options selected.

    Methods
    -------
    start()
        call the view method to render the GUI.
    generate_password(keyword,ckbs,length)
        Returns a new password.
    build_set(ckbs_status)
        Returns a set of characters.
    """

    def __init__(self):
        self.file_manager = FileManager(self)
        keys = getattr(self.file_manager, 'set_space').keys()
        if keys is None:
            logger.error('Fail to retrieve keys from the model')
        logger.debug('keys from model: '+','.join(keys))
        self.main_frame = MainFrame(self, keys)
        # store the current password shown in the view
        self.current_password = None
        # store the current options to create new password
        self.final_set = None

    def start(self):
        '''calls the view to render GUI'''
        self.main_frame.display_panel()

    def generate_password(self, keyword, ckbs, length):
        '''Creates a new password by creating a Password instance
        and  forwards it to the view'''
        # use previous config if nothing has changed
        if ckbs != self.final_set:
            self.final_set = self.update_set(ckbs)
            logger.info('password settings not changed')
        length = int(length)  # combobox returns strings
        # Create new password and store it
        self.current_password = Password(keyword, self.final_set, length)
        # update view with the new password
        logger.info('Delivering new password to view')
        self.main_frame.set_password(getattr(self.current_password, 'value'))

    def update_set(self, ckbs_status):
        '''extract setting selected from the view and queries
        the model to build the final charset to
        create the new password.

        Parameters
        ----------
        ckbs_status : dict
        dict containing the keys and the intVar variables of the view.

        Returns
        ----------
        final_set : set
        Unions on similar sets do not modify the final set.
        The second case accounts for the cases of deactivating a ckbs.
        empty is needed for the first generated password.
        '''
        final_set = self.file_manager.default
        logger.info('Acessing model sets')
        for key, var in ckbs_status.items():
            current_set = self.file_manager.get_set(key)
            intersection = final_set.intersection(current_set)
            if var.get() == 1 and key != 'exclude':
                final_set = final_set.union(current_set)
            elif var.get() == 0 and key != 'exclude':
                if intersection != set():
                    final_set = final_set.symmetric_difference(current_set)
            elif var.get() == 1 and key == 'exclude':
                logger.info('Exclude option activated')
                final_set = final_set.symmetric_difference(intersection)
        return final_set


if __name__ == '__main__':
    controller = Relayer()
