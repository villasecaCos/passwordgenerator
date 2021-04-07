#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:53:46 2021

@author: juan
"""
import tkinter as tk

class PanelOptionMenu(tk.Frame):
    
    PADX,PADY = 5,5
    DEFAULT = 10
    
    labels = [
            'Length'
            ]
    
    def __init__(self,master):
        super(). __init__(master=master)
        self.length = tk.IntVar()
        self.length.set(self.DEFAULT)
        self.create_panel()
        
    def create_panel(self):
        for label in self.labels:
            self.add_optionmenu(label)
        self.pack()
        
    # create label and dropdown menu in the root window
    def add_optionmenu(self,name):
        frm = tk.Frame(master=self)
        frm.pack(padx = self.PADX,pady = self.PADY)
        #'length' label
        lbl = tk.Label(master=frm, text=name, padx=self.PADX)
        lbl.pack(side=tk.LEFT)
        #drop-down menu to choose password length
        options = [x for x in range(6,30)]
        opt = tk.OptionMenu(frm, self.length, *options )
        opt.config(width = 20, font=('Helvetica', 10))
        opt.pack(side=tk.LEFT)
         
       