#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:07:35 2021

The controller collects the preferences of the user from the View,
collect the value of that preferences of the Model and creates a new
password. 

@author: juan Villaseca
"""

import logging
from controller.password import Password
from view.main_frame import MainFrame
from model.file_manager import FileManager

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

FORMAT = '%(asctime)s:%(module)s:%(levelname)s:%(message)s'
formatter = logging.Formatter(FORMAT)

file_handler = logging.FileHandler('controller.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class Relayer():
    
    def __init__(self):
        self.file_manager = FileManager(self)
        keys = getattr(self.file_manager,'set_space').keys()
        logger.debug('keys from model: '+','.join(keys))
        self.main_frame = MainFrame(self,keys)
        #store the current password shown in the view
        self.current_password = None
        
    def start(self):
        #creates the GUI for the user
        self.main_frame.display_panel()
    
    # generate password pipeline
    def generate_password(self,keyword,ckbs,length):
        #collecting parameteres from the view
        final_set = self.build_set(ckbs)
        length = int(length)
         #Create new password and store it
        self.current_password = Password(keyword,final_set,length)
        #update view with the new password
        logger.info('Delivering new password to view')
        self.main_frame.set_password(self.current_password.value)
                
    #queries the model and build the charset to generate new random password
    def build_set(self, ckbs_status):
        final_set = self.file_manager.default
        logger.info('Acessing model sets')
        for key,_var in ckbs_status.items():
            if _var.get() == 1 and key != 'exclude':
                #concatenate selected sets
                final_set = final_set.union(self.file_manager.get_set(key))
            elif _var.get() == 1 and key == 'exclude':
                logger.info('Exclude option activated')
                final_set = final_set.symmetric_difference(self.file_manager.get_set(key))
        return final_set
    
    
if __name__ == '__main__':
     controller = Relayer()
     
     
