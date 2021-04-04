#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 07:35:48 2021

The MainFrame is reponsible of displaying the information.
The MainFrame contain all the second level frames. 

@author: juan Villaseca

"""

import tkinter as tk
from view.panel_ckbs import PanelCkbs


class MainFrame(tk.Tk):
    
    ent_label = 'Keyword'
    spb_label = 'Length'
    #Panel geometry
    WINDOW_SIZE = ['400','400']#[x,y] in pixels
    PADX = 5 #horizontal distance between 2 widgets
    PADY = 5 #vertical distance between 2 widgets
    # options for widgets
    READONLY = 'readonly'#block write mode in widgets
    
    def __init__(self, controller): 
        super().__init__()#inherits from TK 
        self.controller = controller
        self.title = 'Password generator'
        self.geometry('x'.join(MainFrame.WINDOW_SIZE))#set the dimension of the windo
        self.panel_ckbs = None
        self.field_var = tk.StringVar()
        self.spin_var = tk.StringVar()
        self.lbl = None #label to display new password
        self.image_copy = None#image on top of the copy button
        self.create_window()
        
    def display_panel(self):
        #renders the GUI
        self.mainloop()
              
    
    #create a label and entry wideget in the root window
    def add_field(self,name):
         #container for field
         frm = tk.Frame(master=self)
         #add frame to the window
         frm.pack(padx = MainFrame.PADX, pady = MainFrame.PADY)
         # master parameter adds a widget to a frame
         lbl_pattern = tk.Label(master = frm, text=name, padx = MainFrame.PADX)
         ent_pattern = tk.Entry(master = frm, textvariable = self.field_var) 
         # place the entry at the right side of the label
         lbl_pattern.pack(side=tk.LEFT)
         ent_pattern.pack(side=tk.LEFT)
          
    # create label and spinbox widget in the root window
    def add_spinbox(self,name,from_, to):
        #container for length field
        frm = tk.Frame(master=self)
        #add frame to the window
        frm.pack(padx = MainFrame.PADX,pady = MainFrame.PADY)
        lbl = tk.Label(master = frm, text=name, padx = MainFrame.PADX)
        spb = tk.Spinbox(master = frm, from_=from_, to=to, textvariable = self.spin_var, state = MainFrame.READONLY)
        lbl.pack(side=tk.LEFT)
        spb.pack(side=tk.LEFT)
    
    
    #Event method
    def notify(self):
        print('Event triggered: checkbutton toggle')
        
    #Event method
    def notify_field(self):
        print('Event triggered: entry update')
        
    #Event method
    # notifies and passes all the values to the controller
    def notify_controller(self):
        self.print_ckbs_status()
        print('Notifying updates to controller...')
        ckbs_vars = getattr(self.ckb_vars,'panel_ckbs')
        self.controller.generate_password(self.field_var, ckbs_vars,self.spin_var )

    #Event method
    # notifies and applies for the current password 
    def copy_password(self):
        current_password = getattr(self.controller, 'current_password')
        if current_password is None:
            print('ERROR: No password to be copied')
        else:
            self.clipboard_clear()
            # text to clipboard
            self.clipboard_append(current_password)
            print('Password copied to clipboard')
            
    #appends all necessary widgets to the root
    def create_window(self):
        print('Making window...')
        #NOT working
        self.panel_ckbs = PanelCkbs(self)
        self.add_field(self.ent_label)
        self.add_spinbox(self.spb_label,6,30)
         # Button to save config and generate password
        btn = tk.Button(master = self, text = "generate password"
                        ,command = self.notify_controller)
        btn.pack(pady = MainFrame.PADY)
        #frame for label and copy button
        frm = tk.Frame(master=self)
        frm.pack()
        #Label for the generated password
        self.lbl = tk.Label(master = self,text='')   
        self.lbl.pack(side=tk.LEFT, pady = MainFrame.PADY
                      ,padx = MainFrame.PADX)
       
        # Button to save config and generate password
        #the path from the controller module
        image_path = './../view/images/copy3.png'
        self.image  = tk.PhotoImage(file = image_path, master = frm)
        btn_copy = tk.Button(master = frm, command = self.copy_password, height = 23, 
          width = 23, image = self.image)
        btn_copy.pack(side=tk.LEFT,pady = MainFrame.PADY)
               
    def error(self,error_code):
        if(error_code == 0):
            print('Not password available to copy')
            
    
if __name__ == '__main__':
    view = MainFrame(None)
    view.display_panel()
