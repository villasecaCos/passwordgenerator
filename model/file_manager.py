#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 15:30:36 2021
Stores the user prerences for the passwords,
and the seed charsets to be input to the password generation process. 
@author: juan Villaseca
"""

class FileManager():
   
    files_Path = '../model/files/'
    default = {'a','b','c','d','e','f','g','h','i','j','k'
               ,'l','m','n','o','p','q','r','s','t','u','v'
               ,'w','x','y','z'}
    
    def __init__(self, controller):
        self.controller = controller
        self.set_space = {}
        self.load_sets()
    
    def load_sets(self):
        print('Loading file content into FileManager')
        with open(self.files_Path+'sets.txt','r') as sets:
            for _set in sets:
                key_value = _set.split()
                self.set_space[key_value[0]] = set(key_value[1])

    def get_set(self, key):  
        return self.set_space[key]
    
    