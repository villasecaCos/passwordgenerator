#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Module that represents the model of the application. It stores
the different sets and pass them to the controller when requested.'''

import logging
import yaml
from pathlib import Path

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

FORMAT = '%(asctime)s:%(module)s:%(levelname)s:%(message)s'
formatter = logging.Formatter(FORMAT)
# create log file
file_handler = logging.FileHandler('model/model.log', mode='w')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class FileManager():
    """
    Loads and stores data. Handles request from the controller.

    ...

    Attributes
    ----------
    controller : Relayer
        Instance of Relayer to forward data to the view module.
    set_space : Dict
        Dictionary that stores the sets information.

    Methods
    -------
    load_sets()
        Load the info in 'sets.txt' to the dictionary set_space.
    get_set(key)
        Returns the value stored in set_space given a key.

    """
    data_folder = Path('model/files/')
    default = {
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z'
               }

    def __init__(self, controller):
        self.controller = controller
        self.set_space = {}
        logger.info(f'Loding sets from: {FileManager.data_folder}')
        self.load_sets()

    def load_sets(self):
        '''Read sets from file and stores the info into a dictionary.

        Raise
        ----------
        FileNotFoundError
            when the path to sets file is not known
        '''
        try:
            data_file = FileManager.data_folder/'charsets.yml'
            f = open(data_file, 'r')
        except FileNotFoundError:
            logger.exception('try to run project from main.py')
        else:
            with f:
                parsed_file = yaml.safe_load(f)
                self.set_space = parsed_file

    def get_set(self, key):
        '''Access the set_space attribute to return requested set.'''
        logger.info(f'Access to set: {key}')
        return self.set_space[key]


if __name__ == '__main__':
    model = FileManager(None)
