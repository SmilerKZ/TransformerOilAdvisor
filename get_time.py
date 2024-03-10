# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 20:29:41 2021

@author: Mukhtar
"""
import time

def get_clock():
    # Reutn hout, minute and second
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    return hour, minute, second

def get_date():
    # Return year, month and day
    year = time.strftime("%Y")
    month = time.strftime("%m")
    day = time.strftime("%d")
    return year, month, day