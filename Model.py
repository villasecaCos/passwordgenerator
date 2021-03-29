#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 15:30:36 2021
Stores the user prerences for the passwords,
and the seed charsets to be input to the password generation process. 
@author: juan Villaseca
"""

class Model():
   
    numbers = '0123456789'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    special = '!|#$~%&¬/()=?¿^+*-[]{}'
    
    def __init__(self, controller):
        self.controller = controller
        
    #not HARD CODING
    def get_set(self, key):  
        if key == 'Numbers':
            return self.numbers
        elif key == 'Uppercase':
            return self.uppercase
        else:
            return self.special
        
    def get_lowercase(self):
            return self.lowercase