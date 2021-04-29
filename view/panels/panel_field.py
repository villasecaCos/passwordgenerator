#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Represents the panel of the fields
"""
import tkinter as tk
from view.panels.panel import Panel

class PanelField(Panel):
    """
    Panel containing fields (Label and Entry widgets). 
    ...
    Class Attributes
    ----------
    PADX : int
        horizontal padding between two widgets. 
    PADY : int
        vertical padding between two widgets. 
    labels : list
        list of labels value to display on the panel. 
      
    Attributes
    ----------
    field : StringVar
        Stores the input of the Entries. 

    Methods
    -------
    create_panel()
        Appends the panel to the main window. 
    add_field(name)
        create one field and appends it to the panel.
    """
   
    labels = [
            'keyword'
            ]
    
    def __init__(self, parent):
        super(). __init__(parent)
        self.field = tk.StringVar()
        self.create_panel()
    
    def create_panel(self):
        '''create all fields and append to main window.'''
        # create container for all fields
        frm = tk.Frame(master=self)
        # add fields to the container
        frm.pack(pady = Panel.panel_PADY)
        for i in self.labels:
            self.add_component(frm, i)
        self.pack() 
            
   
    def add_component(self, parent, name):
         '''Create a field with padding specifications'''
         # create container for field
         frm = tk.Frame(master=parent)
         # add container to the panel
         frm.pack(padx = Panel.PADX, pady = Panel.PADY)
         # create field
         lbl_pattern = tk.Label(master = frm, text=name, padx = Panel.PADX)
         ent_pattern = tk.Entry(master = frm, textvariable = self.field) 
         # add field to container
         lbl_pattern.pack(side=tk.LEFT)
         ent_pattern.pack(side=tk.LEFT)