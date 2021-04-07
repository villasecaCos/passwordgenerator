#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 15:30:36 2021
Stores the user prerences for the passwords,
and the seed charsets to be input to the password generation process. 
@author: juan Villaseca
"""

class FileManager():
   
    numbers = {'0','1','2','3','4','5','6','7','8','9'}
    
    lowercase = {'a','b','c','d','e','f','g','h'
                 ,'i','j','k','l','m','n','o','p'
                 ,'q','r','s','t','u','v','w','x'
                 ,'y','z'}
    
    uppercase = {'A','B','C','D','E','F','G','H','I'
                 ,'J','K','L','M','N','O','P','Q','R'
                 ,'S','T','U','V','W','X','Y','Z'}
    
    special = {'!','|','#','$','~','%','&','¬','/'
               ,'(',')','=','?','¿','^','+','*','-'
               ,'[',']','{','}'}
    
    def __init__(self, controller):
        self.controller = controller
        
    #not HARD CODING
    def get_set(self, key):  
        if key == '(0,1,2....9)':
            return self.numbers
        elif key == '(A,B,C....Z)':
            return self.uppercase
        else:
            return self.special
        
    def get_lowercase(self):
            return self.lowercase