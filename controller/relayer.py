#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:07:35 2021

The controller collects the preferences of the user from the View,
collect the value of that preferences of the Model and creates a new
password. 

@author: juan Villaseca
"""

from password import Password
from view.main_frame import MainFrame
from model.file_manager import FileManager


class Relayer():
    
    def __init__(self):
        self.file_manager = FileManager(self)
        keys = getattr(self.file_manager,'set_space').keys()
        self.main_frame = MainFrame(self,keys)
        #store the current password shown in the view
        self.current_password = None
        
    def start(self):
        #creates the GUI for the user
        self.main_frame.display_panel()
    
    # generate password pipeline
    def generate_password(self,keyword_var,ckbs,length_var):
        #collecting parameteres from the view
        keyword = keyword_var.get()
        final_set = self.build_set(ckbs)
        length = length_var.get()
         #Create new password and store it
        self.current_password = Password(keyword,final_set,length)
        print('New password generated')
        #update view with the new password
        self.main_frame.set_password_lbl(self.current_password.value)
                
    #queries the model and build the charset to generate new random password
    def build_set(self, ckbs_status):
        final_set = self.file_manager.default
        print('Accessing model sets')
        for key,_var in ckbs_status.items():
            if _var.get() == 1 and key != 'exclude':
                final_set += self.file_manager.get_set(key)#union of sets
            elif _var.get() == 1 and key == 'exclude':
                self.exclude_string(final_set, self.file_manager.get_set(key))
        return final_set
    
    def exclude_string(self, charset, exclude):
        for x in exclude:
            charset.replace(x,"")
    
if __name__ == '__main__':
     controller = Relayer()
     controller.start()
     
