u# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12
Modified on Sat Mar 7

@author1: Mukhtar Turarbek
@author2: Dinmukhammedali Otynshy
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import entry_placeholder as ep
import mineral_oil_analysis as moa


    
def full_analysis():
    # Make full analysis of parameters
    
    
    # Check if numbers are entered to entries, except serial numbers entry
    try:
        # Take parameters (strings ) from entries to variables
        # Convert parameters from string to float
        tx_v = float(entry_tx_V.get())
        dbv = float(entry_dbv.get())
        gap = float(entry_gap.get())
        if entry_temp.get() == "less than 25": temp = 25
        else: temp = 100
        factor = float(entry_factor.get())
        tension = float(entry_tension.get())
        neutr = float(entry_neutr.get())
        water = float(entry_water.get())
        oxid = float(entry_oxid.get())
        
        # Take strings from entries
        serial_num = entry_serial_num.get()
        oil = oil_type.get()
        
        
        # Conduct parameters check according to the voltage class
        if tx_v <= 69:
            moa.low_voltage(serial_num, oil, tx_v, dbv, gap, temp, factor, tension, neutr, water, oxid, root)
    
        elif 69 < tx_v < 230:
            moa.medium_voltage(serial_num, oil, tx_v, dbv, gap, temp, factor, tension, neutr, water, oxid, root)
    
        elif tx_v >= 230:
            moa.high_voltage(serial_num, oil, tx_v, dbv, gap, temp, factor, tension, neutr, water, oxid, root)
    
    # If numbers are not entered to necessary entries
    except ValueError:
        # Give warning message
        messagebox.showinfo("", "Type numbers on entries")

def wrong_oil(event):
    # Give warning message for other oil types than mineral oil type
    if oil_type.get() == "Stern Oil" or oil_type.get() == "Synthetic Oil":
        messagebox.showinfo("", "The chosen oil type doesn't implemented\nIt will be implemented in the future")


# Create root
root = Tk()
root.title("Transformer Oil Analysis")
root.configure(background="white")
root.geometry('600x500')

# Print label
Label(root, text="TRANSFORMER OIL ANALYSIS\n(IEEE Std. C57.106-2015)", bg="white", font="Times 18 bold").grid(columnspan=3)#row=0, column=0)

# Draw a line
separator = ttk.Separator(root, orient='horizontal').grid(row=1, columnspan=5, sticky="ew", pady=15)


# Serial number
# Label
serial_num = Label(root, text="Serial number: ", bg="white", font="Times 13")
serial_num.grid(row=2, column=0, sticky=W)
# Entry
entry_serial_num = ep.EntryWithPlaceholder(root, placeholder="Entry Serial Number")
entry_serial_num.grid(row=2, column=1)


# Transformer Insulation Oil
# Label
Label(root, text="Transformer insulation oil: ", bg="white", font="Times 13").grid(row=4, column=0, sticky=W)
oils = ["Stern Oil", "Synthetic Oil", "Mineral Oil"]
# Combobox
oil_type = ttk.Combobox(root, value=oils)
oil_type.current(2)
oil_type.bind("<<ComboboxSelected>>", wrong_oil)
oil_type.grid(row=4, column=1, sticky=W)


# Transformer Voltage class in kV
# Label
par_tx_V = Label(root, text="Voltage of a transformer [kV]", bg="white", font="Times 13")
par_tx_V.grid(row=5, column=0, sticky=W)
# Entry
entry_tx_V = ep.EntryWithPlaceholder(root, placeholder="Entry Voltage Class")
entry_tx_V.grid(row=5, column=1)


# Dielectric voltage breakdown
# Label
par_dbv = Label(root, text="Dielectric breakdown voltage [kV minimum]", bg="white", font="Times 13")
par_dbv.grid(row=6, column=0, sticky=W)
# Entry
entry_dbv = ep.EntryWithPlaceholder(root, placeholder="Entry Breakdown Voltage")
entry_dbv.grid(row=6, column=1)


# Gap Distance
# Label
par_gap = Label(root, text="Gap distance [mm]", bg="white", font="Times 13")
par_gap.grid(row=7, column=0, sticky=W)
# Entry
gaps = [1, 2]
entry_gap = ttk.Combobox(root, value=gaps)
entry_gap.current(0)
entry_gap.grid(row=7, column=1, sticky=W)


# Dissipation Factor (power factor)
# Label
par_factor = Label(root, text="Dissipation factor (power factor)", bg="white", font="Times 13")
par_factor.grid(row=8, column=0, sticky=W)
# Entry
entry_factor = ep.EntryWithPlaceholder(root, placeholder="Entry Power Factor")
entry_factor.grid(row=8, column=1)


# Temperature
# Label
par_factor = Label(root, text="Temperature [Celsius]", bg="white", font="Times 13")
par_factor.grid(row=9, column=0, sticky=W)
# Entry
temps = ["less than 25", "more than 25"]
entry_temp = ttk.Combobox(root, value=temps)
entry_temp.current(0)
entry_temp.grid(row=9, column=1, sticky=W)



# Interfacial_tension
# Label
par_tension = Label(root, text="Interfacial tension [mN/m minimum]", bg="white", font="Times 13")
par_tension.grid(row=10, column=0, sticky=W)
# Entry
entry_tension = ep.EntryWithPlaceholder(root, placeholder="Entry Interfacial Tension")
entry_tension.grid(row=10, column=1)


# Neutralization number
# Label
par_neutr = Label(root, text="Neutralization number (acidity) [mg KOH/g maximum]", bg="white", font="Times 13")
par_neutr.grid(row=11, column=0, sticky=W)
# Entry
entry_neutr = ep.EntryWithPlaceholder(root, placeholder="Entry Neutralization Number")
entry_neutr.grid(row=11, column=1)

# Water content
# Label
par_water = Label(root, text="Water content [mg/kg maximum (ppm)]", bg="white", font="Times 13")
par_water.grid(row=12, column=0, sticky=W)
# Entry
entry_water = ep.EntryWithPlaceholder(root, placeholder="Entry Water Content")
entry_water.grid(row=12, column=1)

# Oxidation inhibitor content
# Label
par_oxid = Label(root, text="Oxidation inhibitor content [%] minimum", bg="white", font="Times 13")
par_oxid.grid(row=13, column=0, sticky=W)
# Entry
entry_oxid = ep.EntryWithPlaceholder(root, placeholder="Entry Ox. Inhibitor content")
entry_oxid.grid(row=13, column=1)


# Analyze transformer oil
# Button
btn_anlz = Button(root, text="Analyze", command=full_analysis, font="Times 13")
btn_anlz.grid(columnspan=3)

# Launch Tkinter
root.mainloop()