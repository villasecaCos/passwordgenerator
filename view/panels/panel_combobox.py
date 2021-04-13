#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:53:46 2021

@author: juan
"""
import tkinter as tk
from tkinter import ttk

class PanelCombobox(tk.Frame):
    
    PADX,PADY = 5,5
    DEFAULT = 10
    
    labels = [
            'Length'
            ]
    
    def __init__(self,master):
        super(). __init__(master=master)
        self.length = tk.StringVar()
        self.create_panel()
        
    def create_panel(self):
        for label in self.labels:
            self.add_combobox(label)
        self.pack()
        
    # create label and dropdown menu in the root window
    def add_combobox(self,name):
        frm = tk.Frame(master=self)
        frm.pack(padx = self.PADX,pady = self.PADY)
        #'length' label
        lbl = tk.Label(master=frm, text=name, padx=self.PADX)
        lbl.pack(side=tk.LEFT)
        #drop-down menu to choose password length
        options = [x for x in range(6,30)]
        combo = ttk.Combobox(master = frm, textvariable = self.length
                             ,values = options)
        combo.set(PanelCombobox.DEFAULT)
        combo.pack(side=tk.LEFT)
         
       