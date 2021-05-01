#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Represents the checkbuttons panel
"""
import tkinter as tk
from view.panels.panel import Panel


class PanelCkbs(Panel):
    """
    Panel containing labels/checkbuttons widgets.
    ...
    Class Attributes
    ----------
    PADX : int
        horizontal padding between two widgets.
    PADY : int
        vertical padding between two widgets.
    labels : list
        list of labels value to display on the panel.
    button_labels : list
        list of labels display at the right of the checkbuttons.

    Attributes
    ----------
    keys: dict_keys
        Keys from the model.
    ckbs_vars : dict
        Store checkbuttons state.

    Methods
    ----------
    create_dict(keys)
        Initialize checkboxes variables to store their states.
    create_panel()
        Appends the panel to the main window.
    add_field(name)
        Create one field and appends it to the panel.
    add_checkbox(label,name,key)
        Create label/checkbutton, and appends them to the panel.
    get_ckbs_status()
        str parsing to log checkbuttons state.
    """

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

    def __init__(self, parent, keys):
        super(). __init__(parent)
        self.keys = keys
        self.ckbs_vars = self.create_dict(keys)
        self.create_panel()

    def create_dict(self, keys):
        '''Create dict with keys of the model and values with IntVar.'''
        dic = dict()
        for key in keys:
            dic[key] = tk.IntVar()
        return dic

    def create_panel(self):
        '''Create all labels/checkbuttons and append panel to main window.'''
        # create container for all label/checkbox
        frm = tk.Frame(master=self)
        # add container to the panel
        frm.pack(pady=Panel.panel_PADY)
        for label, button_label, key in zip(self.labels,
                                            self.button_labels, self.keys):
            self.add_component(frm, label, button_label, key)
        self.pack()

    def add_component(self, parent, label, name, key):
        '''Create one label/checkbutton and append to the panel.'''
        # create container for label/checkbox
        frm = tk.Frame(master=parent)
        # add container to the panel
        frm.pack(padx=Panel.PADX, pady=Panel.PADY)
        # create label/checkbox
        lbl = tk.Label(master=frm, text=label, padx=self.PADX)
        ck_numbers = tk.Checkbutton(master=frm, text=name, onvalue=1,
                                    offvalue=0, variable=self.ckbs_vars[key])
        # add label/checkbutton to container
        lbl.pack(side=tk.LEFT, padx=Panel.PADX)
        ck_numbers.pack(side=tk.LEFT)

    def get_ckbs_status(self):
        '''str representation of the checkbuttons state.'''
        ckbs = ''
        for key, value in self.ckbs_vars.items():
            ckbs += ' '+key+': '+str(value.get())
        return ckbs
