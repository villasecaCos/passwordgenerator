#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Represents a password and the settings used to create it. 
"""
import random

class Password():
    """
    password entity. 
    ...

    Attributes
    ----------
    charset : set
        Instance of the model. 
    length : int
        keys of the underlying data model(a dictionary) of the model. 
    keyword : str
        Instance of the view. 
    value : str
        the actual password.

    Methods
    -------
    compute_password(keyword, charset, length)
        creates new password. 
    """
    def __init__(self, keyword, charset, length):
        self.charset = charset
        self.length = length
        self.keyword = keyword
        self.value = self.compute_password(keyword,charset,length)
    
    def compute_password(self, keyword, charset, length):
        '''concatenates randomly characters extracted from charset.
        if keyword is not none it is appended at the beggining of
        the password. 
        Parameters
        ----------
        keyword : str
        dict containing the keys and the intVar variables of the view. 
        charset : set
        set of characters
        length : int
        length of the final password plus the length of the keyword
        
        Returns
        ----------
        new_password : str
        contains the created password. 
        '''
        new_password = ""
        if keyword is not None:
            new_password += keyword
        #generate the password
        for i in range(length):
            new_character = random.choice(tuple(charset))
            new_password += new_character
        return new_password
    
    
        