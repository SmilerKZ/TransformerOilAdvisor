# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 19:50:49 2021

@author: Mukhtar
"""
from tkinter import *

class EntryWithPlaceholder(Entry):
    # Create placeholders for entries
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']
        self.default_bd = 5
        self.default_font = "none 13"
        # If clicked on it, then remove placeholder
        self.bind("<FocusIn>", self.foc_in)
        # Check if something is typed
        self.bind("<FocusOut>", self.foc_out)
        # Put placeholder 
        self.put_placeholder()
        
        
    def put_placeholder(self):
        # Put placeholder 
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color
        self['bd'] = self.default_bd
        self['font'] = self.default_font


    def foc_in(self, *args):
        # If clicked on it, then remove placeholder
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        # Check if something is typed
        if not self.get():
            self.put_placeholder()