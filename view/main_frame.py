#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 07:35:48 2021

The MainFrame is reponsible of displaying the information.
The MainFrame contain all the second level frames. 

@author: juan Villaseca

"""

import tkinter as tk
from view.panels.panel_ckbs import PanelCkbs
from view.panels.panel_field import PanelField
from view.panels.panel_optionmenu import PanelOptionMenu


class MainFrame(tk.Tk):
    
   
    #Main window geometry
    WINDOW_SIZE = ['400','400']#[x,y] in pixels
    PADX = 5 #horizontal distance between 2 widgets
    PADY = 5 #vertical distance between 2 widgets
    # options for widgets
    READONLY = 'readonly'#block write mode in widgets
    
    def __init__(self, controller): 
        super().__init__()#inherits from TK 
        self.controller = controller
        self.title('Password generator')
        self.geometry('x'.join(MainFrame.WINDOW_SIZE))#set the dimension of the windo
        self.panel_ckbs = None
        self.lbl = None #label to display new password
        self.image_copy = None#image on top of the copy button
        self.create_window()
        
    def display_panel(self):
        #renders the GUI
        self.mainloop()
               
    #Event method
    def notify(self):
        print('Event triggered: checkbutton toggle')
        
    #Event method
    def notify_field(self):
        print('Event triggered: entry update')
        
    #Event method
    # notifies and passes all the values to the controller
    def notify_controller(self):
        print('Notifying updates to controller...')
        ckbs_vars = getattr(self.panel_ckbs,'ckbs_vars')
        keyword = getattr(self.panel_field,'field')
        length = getattr(self.panel_scrollbar,'length')
        self.controller.generate_password(keyword, ckbs_vars,length )

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
        self.panel_ckbs = PanelCkbs(self)
        self.panel_field = PanelField(self)
        self.panel_scrollbar = PanelOptionMenu(self)
         # Button to save config and generate password
        btn = tk.Button(master = self, text = "generate password"
                     ,command = self.notify_controller)
        btn.pack(pady = MainFrame.PADY,side=tk.LEFT)
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
        btn_copy = tk.Button(master = frm, command = self.copy_password
                    , height = 23, width = 23, image = self.image)
        btn_copy.pack(side=tk.LEFT,pady = MainFrame.PADY)
               
    def error(self,error_code):
        if(error_code == 0):
            print('Not password available to copy')
            
    
if __name__ == '__main__':
    view = MainFrame(None)
    view.display_panel()
