#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:52:51 2021

@author: juan
"""
import tkinter as tk

class PanelField(tk.Frame):
    
    PADX,PADY = 5,5
    
    labels = [
            'keyword'
            ]
    
    def __init__(self, master):
        super(). __init__(master=master)
        self.master = master
        self.field = tk.StringVar()
        self.create_panel()
    
    def create_panel(self):
        for i in self.labels:
            self.add_field(i)
        self.pack()
            
    #create a label and entry wideget in the root window
    def add_field(self,name):
         #container for field
         frm = tk.Frame(master=self)
         #add frame to the window
         frm.pack(padx = self.PADX, pady = self.PADY)
         # master parameter adds a widget to a frame
         lbl_pattern = tk.Label(master = frm, text=name, padx = self.PADX)
         ent_pattern = tk.Entry(master = frm, textvariable = self.field) 
         # place the entry at the right side of the label
         lbl_pattern.pack(side=tk.LEFT)
         ent_pattern.pack(side=tk.LEFT)