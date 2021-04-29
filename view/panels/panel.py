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
    
    def __init__(self,parent):
        super().__init__(parent)
        
    @abstractmethod
    def create_panel(self):
      pass
    @abstractmethod
    def add_component(self):
      pass
  
