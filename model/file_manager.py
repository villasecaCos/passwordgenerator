#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 15:30:36 2021
Stores the user prerences for the passwords,
and the seed charsets to be input to the password generation process. 
@author: juan Villaseca
"""
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

FORMAT = '%(asctime)s:%(module)s:%(levelname)s:%(message)s'
formatter = logging.Formatter(FORMAT)

file_handler = logging.FileHandler('model/model.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class FileManager():
   
    files_path = 'model/files/'
    default = {'a','b','c','d','e','f','g','h','i','j','k'
               ,'l','m','n','o','p','q','r','s','t','u','v'
               ,'w','x','y','z'}
    
    def __init__(self, controller):
        self.controller = controller
        self.set_space = {}
        logger.info(f'Loding sets from: {FileManager.files_path}')
        self.load_sets()
    
    def load_sets(self):
        try:
            with open(FileManager.files_path+'sets.txt','r') as sets:
                for _set in sets:
                    key_value = _set.split()
                    self.set_space[key_value[0]] = set(key_value[1])
                    logger.debug(f'set {key_value[0]} composed by '
                                        + f'[{key_value[1]}]')
        except FileNotFoundError:
            logger.exception('try to run project from main.py')

    def get_set(self, key):  
        logger.info(f'Access to set: {key}')
        return self.set_space[key]
    
if __name__ == '__main__':
    model = FileManager(None)
    