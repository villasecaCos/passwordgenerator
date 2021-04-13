#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 07:35:48 2021

The MainFrame is reponsible of displaying the information.
The MainFrame contain all the second level frames. 

@author: juan Villaseca

"""

import tkinter as tk
import logging
from view.panels.panel_ckbs import PanelCkbs
from view.panels.panel_field import PanelField
from view.panels.panel_optionmenu import PanelCombobox
from view.panels.panel_buttons import PanelButtons


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

FORMAT = '%(asctime)s:%(module)s:%(levelname)s:%(message)s'
formatter = logging.Formatter(FORMAT)

file_handler = logging.FileHandler('view.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class MainFrame(tk.Tk):
    
    #Main window geometry
    GEOMETRY = [400,350]#[width,height] in pixels
    PADX = 5 #horizontal distance between 2 widgets
    PADY = 5 #vertical distance between 2 widgets
    # options for widgets
    READONLY = 'readonly'#block write mode in widgets
    
    def __init__(self, controller,keys): 
        super().__init__()#inherits from TK 
        self.controller = controller
        self.keys = keys
        self.title('Password generator')
        self.geometry(self.convert_w_h())#set the dimension of the window
        self.panel_ckbs = None
        self.panel_opt = None
        self.ent_output = tk.StringVar() #entry to display new password
        self.image_copy = None#image on top of the copy button
        self.create_window()
        
    def display_panel(self):
        #renders the GUI
        self.mainloop()
   
    #Event method
    # notifies and passes all the values to the controller
    def notify_controller(self):
        logger.info('Notifying updates to controller')
        ckbs_vars = getattr(self.panel_ckbs,'ckbs_vars')
        keyword_var = getattr(self.panel_field,'field')
        keyword = keyword_var.get()
        if keyword is None:
            logger.debug(f'sent keyword {keyword_var.get()} to controller')
        else:
            logger.debug(f'sent NO keyword to controller')
        length_var = getattr(self.panel_opt,'length')
        length = length_var.get()
        logger.debug(f'sent length {length} to controller')
        self.controller.generate_password(keyword, ckbs_vars,length )

    #Event method
    # notifies and applies for the current password 
    def copy_password(self): 
        current_password = getattr(self.controller, 'current_password')
        password_value = getattr(current_password, 'value')
        if current_password is None:
            logger.warning('No password to be copied')
        else:
            self.clipboard_clear()
            # text to clipboard
            self.clipboard_append(password_value)
            logger.info('Password copied to clipboard')
            
    #appends all necessary widgets to the root
    def create_window(self):
        logger.info('Making window')
        self.panel_ckbs = PanelCkbs(self,self.keys)
        self.panel_field = PanelField(self)
        self.panel_opt = PanelCombobox(self)
        self.panel_buttons = PanelButtons(self)
        #Label for the generated password
        ent = tk.Entry(master = self,text=self.ent_output
                       ,width=30, state=MainFrame.READONLY)   
        ent.pack(pady = self.PADY, padx = self.PADX)
    
    def set_password(self, new_password):
        logger.info('Displaying new password')
        self.ent_output.set(new_password)

    def convert_w_h(self): 
        return 'x'.join(map(str, MainFrame.GEOMETRY))
            
    
if __name__ == '__main__':
    keys = ['numbers','uppercase','special','exclude']
    view = MainFrame(None,keys)
    view.display_panel()
