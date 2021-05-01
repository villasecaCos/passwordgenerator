#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 22:49:27 2021

@author: juan
"""

import tkinter as tk


class PanelEnt(tk.Frame):
    """
    Panel containing fields (Label and Entry widgets).
    ...
    Class Attributes
    ----------
    PADX : int
        horizontal padding between two widgets.
    PADY : int
        vertical padding between two widgets.
    ENT_WIDTH : int
        the max. length that the entry takes.
    READONLY : str
        block user input in a widget suuch entries or spinboxes.

    Attributes
    ----------
    ent : StringVar
        Stores the input of the Entries.

    Methods
    -------
    create_panel()
        Appends the panel to the main window.
    add_field(name)
        create one field and appends it to the panel.
    """

    PADX, PADY = 5, 5
    panel_PADY = 5
    ENT_WIDTH = 30
    READONLY = 'readonly'

    def __init__(self, parent):
        super().__init__(parent)
        self.ent = None
        self.output = tk.StringVar()
        self.create_panel()

    def create_panel(self):
        '''create ent to display password and append entry.'''
        # container for the entry
        container = tk.Frame(self)
        container.pack(pady=self.panel_PADY)
        # scrollbar to avoid length issues
        sb = tk.Scrollbar(master=container, orient=tk.HORIZONTAL)
        sb.pack(side="bottom", fill="x")

        # entry for the generated password
        self.ent = tk.Entry(master=container, text=self.output,
                            width=PanelEnt.ENT_WIDTH,
                            state=PanelEnt.READONLY, xscrollcommand=sb.set)
        self.ent.focus()
        self.ent.insert("end", str(dir(tk.Scrollbar)))
        self.ent.pack(pady=self.PADY, padx=self.PADX)

        sb.config(command=self.ent.xview)
        self.ent.config()
        self.pack()
