#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 00:13:05 2021

@author: juan
"""
import tkinter as tk
from abc import abstractmethod

class Panel(tk.Frame):
    
    PADX,PADY = 5, 5
    panel_PADY = 10
    
    @abstractmethod
    def create_panel(self):
      pass
  
    @abc.abstractmethod
    def area(self):
      pass