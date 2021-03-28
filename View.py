#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 07:35:48 2021

@author: juan Villaseca
View class implements GUI with library tkinter.
GUI has checkboxes, field(label + entry),  label + spinbox, 2 buttons, label
The widgets above are in order and they all are arranged inside a frame.
"""

import tkinter as tk

class View(tk.Tk):
    
    
    WINDOW_SIZE = ['300','250']#in pixels
    PADX = 5 #horizontal distance between 2 widgets
    PADY = 5 #vertical distance between 2 widgets
    READONLY = 'readonly'#block write mode in widgets
    
    def __init__(self, controller,title, ckbs_names, field_name, spin_name): 
        super().__init__()#inherits from TK 
        self.controller = controller
        self.geometry('x'.join(View.WINDOW_SIZE))#set the dimension of the window  
        self.title(title)#set the title of the main window      
        self.ckbs_names = ckbs_names
        self.ckbs_vars = self.create_dict(ckbs_names)
        self.field_name = field_name
        self.field_var = tk.StringVar()
        self.spin_name = spin_name
        self.spin_var = tk.StringVar()
        self.lbl = None #label to display new password
        self.image = None#image on top of the copy button
        self.create_panel()
        
    def display_panel(self):
        #renders the GUI
        self.mainloop()
               
    #Initialize checkboxes variables to store their states
    def create_dict(self, keys):
        dic = dict()
        for key in keys:
            dic[key] = tk.IntVar()
        return dic
    
    #create a label and entry wideget in the root window
    def add_field(self,name):
         #container for field
         frm = tk.Frame(master=self)
         #add frame to the window
         frm.pack(padx = View.PADX, pady = View.PADY)
         # master parameter adds a widget to a frame
         lbl_pattern = tk.Label(master = frm, text=name, padx = View.PADX)
         ent_pattern = tk.Entry(master = frm, textvariable = self.field_var) 
         # place the entry at the right side of the label
         lbl_pattern.pack(side=tk.LEFT)
         ent_pattern.pack(side=tk.LEFT)
         
    # create checkbox widget in the root window
    def add_checkbox(self,name):
        #container for checkbox
        frm = tk.Frame(master=self)
        #add frame to the window
        frm.pack(padx = View.PADX,pady = View.PADY)
        ck_numbers = tk.Checkbutton(master = frm, text=name, onvalue=1, offvalue=0,variable = self.ckbs_vars[name],command=self.notify)
        ck_numbers.pack()
      
    # create label and spinbox widget in the root window
    def add_spinbox(self,name,from_, to):
        #container for length field
        frm = tk.Frame(master=self)
        #add frame to the window
        frm.pack(padx = View.PADX,pady = View.PADY)
        lbl = tk.Label(master = frm, text=name, padx = View.PADX)
        spb = tk.Spinbox(master = frm, from_=from_, to=to, textvariable = self.spin_var, state = View.READONLY)
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
        self.controller.generate_password(self.get_ckbs_status(),self.get_field_status(),self.get_spinbox_status())

    #Event method
    # notifies and applies for the current password 
    def copy_password(self):
        current_password = self.controller.get_current_password()
        if current_password is None:
            print('ERROR: No password to be copied')
        else:
            self.clipboard_clear()
            # text to clipboard
            self.clipboard_append(current_password)
            print('Password copied to clipboard')
            
    #appends all necessary widgets to the root
    def create_panel(self):
        print('Making window...')
        #create widgets
        for i in self.ckbs_names:
            self.add_checkbox(i)
        self.add_field(self.field_name)
        self.add_spinbox(self.spin_name,6,30)
        #frame for the buttons
        frm = tk.Frame(master=self)
        frm.pack()
        # Button to save config and generate password
        btn = tk.Button(master = frm, text = "generate password",command = self.notify_controller)
        btn.pack(side=tk.LEFT,pady = View.PADY, padx = View.PADX)
        # Button to save config and generate password
        self.image  = tk.PhotoImage(file = "images/copy3.png", master = frm)
        btn_copy = tk.Button(master = frm, command = self.copy_password, height = 23, 
          width = 23, image = self.image)
        btn_copy.pack(side=tk.LEFT,pady = View.PADY)
        #Label for the generated password
        self.lbl = tk.Label(master = self,text='')   
        self.lbl.pack(pady = View.PADY)
        
    def error(self,error_code):
        if(error_code == 0):
            print('Not password available to copy')
            
    # getter for the checkboxes states
    def get_ckbs_status(self):
        return self.ckbs_vars
    
    #getter for the keyword value
    def get_field_status(self):
        return self.field_var
    
    #getter for the spinbox value
    def get_spinbox_status(self):
        return self.spin_var
    
    #setter for the password label
    def set_password_lbl(self,new_password):
        self.lbl['text'] = new_password
        
    def print_ckbs_status(self):
        for key,value in self.ckbs_vars.items():
            print('checkbutton {} state {}'.format(key,value.get()))

if __name__ == '__main__':
    view = View(None, 'view', ['ck1','ck2','ck2'], 'field','spinbox')
    view.display_panel()
