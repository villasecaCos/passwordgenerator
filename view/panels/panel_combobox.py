#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Represents panel the combobox- 
"""
import tkinter as tk
from tkinter import ttk

class PanelCombobox(tk.Frame):
    """
    Panel containing combobox widgets. 
    ...
    Class Attributes
    ----------
    PADX : int
        horizontal padding between two widgets. 
    PADY : int
        vertical padding between two widgets. 
    DEFAULT : int
        default length to display on combobox. 
    labels : list
        list of labels to display on the left of the comboboxes. 
   
    Attributes
    ----------
    length : StringVar
        desired length of password.  

    Methods
    ----------
    create_panel()
        Appends the panel to the main window. 
    add_combobox(name)
        Create label/combobox, and appends them to the panel. 
        
    """
    PADX,PADY = 5,5
    panel_PADY = 5
    DEFAULT = 10
    
    labels = [
            'Length'
            ]
    
    def __init__(self,master):
        super(). __init__(master=master)
        self.length = tk.StringVar() # Combobox coerce StringVar
        self.create_panel()
        
    def create_panel(self):
        '''Create comboboxes and append panel to main window.'''
        frm = tk.Frame(master=self)
        frm.pack(padx = self.PADX,pady = self.panel_PADY)
        for label in self.labels:
            self.add_component(frm, label)
        self.pack()
        
    def add_component(self, parent, name):
        '''Create label/combobox and append it to the panel.'''
        # create container of label/combobox
        frm = tk.Frame(master=self)
        frm.pack(padx = self.PADX,pady = self.PADY)
        # add label to container
        lbl = tk.Label(master=frm, text=name, padx=self.PADX)
        lbl.pack(side=tk.LEFT)
        #drop-down menu to choose password length
        options = [x for x in range(6,30)]
        combo = ttk.Combobox(master = frm, textvariable = self.length
                             ,values = options)
        combo.set(PanelCombobox.DEFAULT)
        combo.pack(side=tk.LEFT)
         
       