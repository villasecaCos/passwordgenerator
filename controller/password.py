#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:01:28 2021
This class represent a password. It creates a password given the 
parameters chosen by the user. 

@author: juan
"""
import random

class Password():
    def __init__(self, keyword, charset, length):
        self.charset = charset
        self.length = length
        self.keyword = keyword
        self.value = self.compute_password(keyword,charset,length)
       
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
    
    
        