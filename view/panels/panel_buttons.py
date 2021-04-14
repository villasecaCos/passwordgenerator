#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Represents the buttons panel. 
"""

import tkinter as tk

class PanelButtons(tk.Frame):
    """
    Panel containing labels/buttons widgets. 
    ...
    Class Attributes
    ----------
    PADX : int
        horizontal padding between two widgets. 
    PADY : int
        vertical padding between two widgets. 
    IMAGES_PATH : str
        path to the images folder. 
   
    Attributes
    ----------
    main_frame : MainFrame
        Instance of the main window. 

    Methods
    ----------
    create_panel()
        Appends the panel to the main window. 
    """
    PADX,PADY = 5,5
    IMAGES_PATH = 'view/panels/images/'
    
    def __init__(self,master):
        super().__init__(master)
        self.main_frame = master # to notify when event triggers
        self.image = None
        self.create_panel()
        
        
    def create_panel(self):
        '''Create buttons and append them to the panel.
        
        Raise
        ----------
         TclError 
             when the image path is not found. 
        '''
        # create container
        frm = tk.Frame(self)
        # add container to panel
        frm.pack()
         # Button to save config and generate password
        btn = tk.Button(master = frm, text = "generate password"
                     ,command = self.main_frame.notify_controller)
        btn.pack(pady = self.PADY,side=tk.LEFT)
        image_name = 'copy3.png'
        # Button to copy the generated password to the clipboard
        try:
            self.image  = tk.PhotoImage(file = self.IMAGES_PATH+image_name
                                        , master = frm)
        except tk.TclError:
            print(f"couldn't open {image_name} no such file")
            print("try to run file from main.py")
        finally:
            btn_copy = tk.Button(master = frm
                    , command = self.main_frame.copy_password
                    , height = 23, width = 23, image = self.image)
            btn_copy.pack(side=tk.LEFT,pady = self.PADY)
            self.pack()