#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 08:51:30 2021

@author: juan
"""

import tkinter as tk

class PanelButtons(tk.Frame):
    
    PADX,PADY = 5,5
    IMAGES_PATH = 'view/panels/images/'
    
    def __init__(self,master):
        super().__init__(master)
        self.main_frame = master
        self.create_panel()
        
        
    def create_panel(self):
        frm = tk.Frame(self)
        frm.pack()
         # Button to save config and generate password
        btn = tk.Button(master = frm, text = "generate password"
                     ,command = self.main_frame.notify_controller)
        btn.pack(pady = self.PADY,side=tk.LEFT)
        # Button to copy the generated password to the clipboard
        try:
            self.image  = tk.PhotoImage(file = self.IMAGES_PATH+'copy3.png', master = frm)
        except:
            print("couldn't open copy3.png no such file")
            print("try to run file from main.py")
        finally:
            btn_copy = tk.Button(master = frm, command = self.main_frame.copy_password
                    , height = 23, width = 23, image = self.image)
            btn_copy.pack(side=tk.LEFT,pady = self.PADY)
            self.pack()