#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 07:46:28 2021

@author: juan

This class creates a panel of checkbuttons. Note that the button 
labels serve as keys to retrieve the state of a checkbutton. 
"""
import tkinter as tk

class PanelCkbs(tk.Frame):
    
    PADX,PADY = 5,5
    
    labels = [
            'Include numbers',
            'Include Uppercase letters',
            'Include special characters',
            'Exclude similar characters',
            ]
    
    button_labels = [
             '(0,1,2....9)',
             '(A,B,C....Z)',
             '($,%,&....})',
             '(I,|,O,0..L)',
             ]
     
    def __init__(self, master,keys):
        super(). __init__(master=master)
        self.keys = keys
        self.ckbs_vars = self.create_dict(keys)
        self.create_panel()
   
        
    #Initialize checkboxes variables to store their states
    def create_dict(self, keys):
        dic = dict()
        for key in keys:
            dic[key] = tk.IntVar()
        return dic
    
    def create_panel(self):
        print("Creating checkbuttons panel")
        for label,button_label,key in zip(self.labels,self.button_labels,self.keys):
            self.add_checkbox(label,button_label,key)
        self.pack()
        
    # create checkbox widget in the root window
    def add_checkbox(self,label,name,key):
        #container for checkbox
        frm = tk.Frame(master=self)
        #create label
        lbl = tk.Label(master = frm, text=label, padx = self.PADX)
        ck_numbers = tk.Checkbutton(master=frm, text=name, onvalue=1
           ,offvalue=0,variable=self.ckbs_vars[key])
        #add frame to the panel
        frm.pack(padx = self.PADX,pady = self.PADY)
        lbl.pack(side=tk.LEFT,padx = self.PADX)
        ck_numbers.pack(side=tk.LEFT)
    
    