#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:07:35 2021

The controller collects the preferences of the user from the View,
collect the value of that preferences of the Model and creates a new
password. 

@author: juan Villaseca
"""

from View import View
from Model import Model
import random

class Controller():
    
    def __init__(self):
        self.model = Model(self)
        self.view = View(self)
        #store the current password shown in the view
        self.current_password = None
    
    def start(self):
        #creates the GUI for the user
        self.view.display_panel()
    
    # generate password pipeline
    def generate_password(self,ckbs,field,spinbox):
        #collecting parameteres from the view
        keyword = field.get()
        final_set = self.build_set(ckbs)
        length = int(spinbox.get())
        #compute new password 
        new_password = self.compute_password(keyword,final_set,length)
        print('New password generated')
        #store new password as current password 
        self.current_password = new_password
        #update view with the new password
        self.view.set_password_lbl(new_password)
                
    #queries the model and build the charset to generate new random password
    def build_set(self, ckbs_status):
        final_set = self.model.get_lowercase()
        print('Accessing model sets')
        for key,_var in ckbs_status.items():
            if _var.get() == 1:
                final_set = final_set + self.model.get_set(key)
        return final_set
    
    # using random indexes of the charset to build new random password
    def compute_password(self, keyword, charset, length):
        new_password = ''
        if keyword is not None:
            new_password = keyword
        #generate the password
        for i in range(length):
            index = random.randint(0,len(charset)-1)
            new_password += charset[index]
        return new_password
                 

if __name__ == '__main__':
     controller = Controller()
     controller.start()
     
