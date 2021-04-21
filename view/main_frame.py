#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Represents the main window of the GUI. 

"""

import tkinter as tk
import logging
from view.panels.panel_ckbs import PanelCkbs
from view.panels.panel_field import PanelField
from view.panels.panel_combobox import PanelCombobox
from view.panels.panel_buttons import PanelButtons
from view.panels.panel_ent import PanelEnt

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

FORMAT = '%(asctime)s:%(module)s:%(levelname)s:%(message)s'
formatter = logging.Formatter(FORMAT)

file_handler = logging.FileHandler('view/view.log', mode='w')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class MainFrame(tk.Tk):
    """
    It coordinates the view and the model. Creates the new passwords. 
    ...
    Class Attributes
    ----------
    GEOMETRY : list
        Defines the size of the main window in pixels. 
    PADX : int
        horizontal padding between two widgets. 
    PADY : int
        vertical padding between two widgets. 
     
        
    Attributes
    ----------
    controller : Relayer
        Instance of the controller. 
    keys : dict_keys
        keys of the underlying data model(a dictionary) of the model. 
    panel_ckbs : PanelCkbs
        instance of the checkbuttons panel. 
    panel_field : PanelField
        instance of the field panel. 
    panel_opt : PanelCombobox  
        instance of the combobox panel. 
    ent_output : Entry
        entry widget to display generated password. 

    Methods
    -------
    display_panel()
        Renders the GUI. 
    notify_controller()
        Forwards users options to the controller.
    copy_password()
        Copy current password to the clipboard. 
    create_window()
        Create the GUI structured to be rendered. 
    set_password(new_password)
        update the current password passed from the controller. 
    convert_w_h()
        convert format to set the geometry correctly. 
    """
    
    GEOMETRY = [400,350] # [width,height] 
    PADX = 5 
    PADY = 5 
    ENT_WIDTH = 30
    READONLY = 'readonly'
    
    def __init__(self, controller,keys): 
        super().__init__()
        self.controller = controller
        self.keys = keys 
        
        self.title('Password generator')
        self.geometry(self.convert_w_h())
        self.resizable(0,0)
        
        self.panel_ckbs = None
        self.panel_field = None
        self.panel_opt = None
        self.create_window()
        
    def display_panel(self):
        '''renders the GUI'''
        self.mainloop()
   
    def notify_controller(self):
        '''Event handler of the create password button'''
        logger.info('Notifying updates to controller')
        # dump attributes into variables
        ckbs_vars = getattr(self.panel_ckbs,'ckbs_vars')
        logger.debug(self.panel_ckbs.get_ckbs_status())
        keyword_var = getattr(self.panel_field,'field')
        keyword = keyword_var.get()
        length_var = getattr(self.panel_opt,'length')
        length = length_var.get()
        # log info
        if keyword is not None:
            logger.debug(f'sent keyword {keyword_var.get()} to controller')
            if len(keyword)+MainFrame.ENT_WIDTH > 30:
                logger.warning("Passoword needs to be scrolled")
        else:
            logger.debug(f'sent NO keyword to controller')
        logger.debug(f'sent length {length} to controller')
        # send info to controller
        self.controller.generate_password(keyword, ckbs_vars,length )

    def copy_password(self): 
        '''Access controller password storage and copies to clipboard'''
        current_password = getattr(self.controller, 'current_password')
        password_value = getattr(current_password, 'value')
        if current_password is None:
            logger.warning('No password to be copied')
        else:
            self.clipboard_clear()
            # text to clipboard
            self.clipboard_append(password_value)
            logger.info('Password copied to clipboard')
            
    def create_window(self):
        '''Append the panels to the main window'''
        logger.info('Making window')
        # create all panels
        self.panel_ckbs = PanelCkbs(self,self.keys)
        self.panel_field = PanelField(self)
        self.panel_opt = PanelCombobox(self)
        self.panel_buttons = PanelButtons(self)
        self.panel_ent = PanelEnt(self)
        
    def set_password(self, new_password):
        """Update the entry with the new password."""
        logger.info('Displaying new password')
        getattr(self.panel_ent, 'output').set(new_password)

    def convert_w_h(self): 
        """Converts list of 2 integers into 'n1xn2' string format."""
        return 'x'.join(map(str, MainFrame.GEOMETRY))
            
    
if __name__ == '__main__':
    keys = ['numbers','uppercase','special','exclude']
    view = MainFrame(None,keys)
    view.display_panel()
