# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 20:11:11 2021

@author: Mukhtar
"""

from tkinter import *
import get_time as gt
from tkinter import ttk
    
def low_voltage(serial_num, oil, tx_v, dbv, gap, temp, factor, tension, neutr, water, oxid, root):
    # Check parameters for low voltage class of mineral oil transformer
    
    
    # Declare dielectric breakdown voltage threshold parameter with respect to gap distance
    if gap == 1:
        normal_low_dbv = 23
    elif gap == 2:
        normal_low_dbv = 40
        
    # Declare dissipation factor threshold parameter with respect to temperature
    if temp <= 25:
        normal_low_factor = 0.5
    elif 25 < temp <= 100:
        normal_low_factor = 5
    
    # Declare thresholds for parameters
    normal_low_tension = 25
    normal_low_neutr = 0.20
    normal_low_water = 35
    normal_low_oxid = 0.08
    
    
    # Check dielectric breakdown voltage
    if dbv < normal_low_dbv:
        dbv_cond = "Unsatisfactory"
    else:
        dbv_cond = "Satisfactory"
        
    # Check dissipation factor
    if factor > normal_low_factor:
        factor_cond = "Unsatisfactory"
    else:
        factor_cond = "Satisfactory"
    
    # Check interfacial tension
    if tension < normal_low_tension:
        tension_cond = "Unsatisfactory"
    else:
        tension_cond = "Satisfactory"
    
    # Chek neutralization number
    if neutr > normal_low_neutr:
        neutr_cond = "Unsatisfactory"
    else:
        neutr_cond = "Satisfactory"
    
    # Check water content
    if water > normal_low_water:
        water_cond = "Unsatisfactory"
    else:
        water_cond = "Satisfactory"
    
    # Check oxidation inhibitor content
    if oxid < normal_low_oxid:
        oxid_cond = "Unsatisfactory"
    else:
        oxid_cond = "Satisfactory"
    
    # Print oil analysis and recommendation
    check_condition(serial_num, oil, tx_v, dbv_cond, factor_cond, tension_cond, neutr_cond, water_cond, oxid_cond, root)


def medium_voltage(serial_num, oil, tx_v, dbv, gap, temp, factor, tension, neutr, water, oxid, root):
    # Check parameters for medium voltage class of mineral oil transformer
    
    # Declare dielectric breakdown voltage threshold parameter with respect to gap distance
    if gap == 1:
        normal_medium_dbv = 28
    elif gap == 2:
        normal_medium_dbv = 47
        
    # Declare dissipation factor threshold parameter with respect to temperature
    if temp <= 25:
        normal_medium_factor = 0.5
    elif 25 < temp <= 100:
        normal_medium_factor = 5
    
    # Declare thresholds for parameters
    normal_medium_tension = 30
    normal_medium_neutr = 0.15
    normal_medium_water = 25
    normal_medium_oxid = 0.08
    
    # Check dielectric breakdown voltage
    if dbv < normal_medium_dbv:
        dbv_cond = "Unsatisfactory"
    else:
        dbv_cond = "Satisfactory"
        
    # Check dissipation factor
    if factor > normal_medium_factor:
        factor_cond = "Unsatisfactory"
    else:
        factor_cond = "Satisfactory"
    
    # Check interfacial tension
    if tension < normal_medium_tension:
        tension_cond = "Unsatisfactory"
    else:
        tension_cond = "Satisfactory"
    
    # Chek neutralization number
    if neutr > normal_medium_neutr:
        neutr_cond = "Unsatisfactory"
    else:
        neutr_cond = "Satisfactory"
    
    # Check water content
    if water > normal_medium_water:
        water_cond = "Unsatisfactory"
    else:
        water_cond = "Satisfactory"
    
    # Check oxidation inhibitor content
    if oxid < normal_medium_oxid:
        oxid_cond = "Unsatisfactory"
    else:
        oxid_cond = "Satisfactory"
    
    # Print oil analysis and recommendation
    check_condition(serial_num, oil, tx_v, dbv_cond, factor_cond, tension_cond, neutr_cond, water_cond, oxid_cond, root)


def high_voltage(serial_num, oil, tx_v, dbv, gap, temp, factor, tension, neutr, water, oxid, root):
    # Check parameters for high voltage class of mineral oil transformer
    
    # Declare dielectric breakdown voltage threshold parameter with respect to gap distance
    if gap == 1:
        normal_high_dbv = 30
    elif gap == 2:
        normal_high_dbv = 50
    
    # Declare dissipation factor threshold parameter with respect to temperature
    if temp <= 25:
        normal_high_factor = 0.5
    elif 25 < temp <= 100:
        normal_high_factor = 5
    
    # Declare thresholds for parameters
    normal_high_tension = 32
    normal_high_neutr = 0.10
    normal_high_water = 20
    normal_high_oxid = 0.08
    
    # Check dielectric breakdown voltage
    if dbv < normal_high_dbv:
        dbv_cond = "Unsatisfactory"
    else:
        dbv_cond = "Satisfactory"
    
    # Check dissipation factor
    if factor > normal_high_factor:
        factor_cond = "Unsatisfactory"
    else:
        factor_cond = "Satisfactory"
    
    # Check interfacial tension
    if tension < normal_high_tension:
        tension_cond = "Unsatisfactory"
    else:
        tension_cond = "Satisfactory"
    
    # Chek neutralization number
    if neutr > normal_high_neutr:
        neutr_cond = "Unsatisfactory"
    else:
        neutr_cond = "Satisfactory"
    
    # Check water content
    if water > normal_high_water:
        water_cond = "Unsatisfactory"
    else:
        water_cond = "Satisfactory"
    
    # Check oxidation inhibitor content
    if oxid < normal_high_oxid:
        oxid_cond = "Unsatisfactory"
    else:
        oxid_cond = "Satisfactory"
    
    # Print oil analysis and recommendation
    check_condition(serial_num, oil, tx_v, dbv_cond, factor_cond, tension_cond, neutr_cond, water_cond, oxid_cond, root)


def check_condition(serial_num, oil, tx_v, dbv_cond, factor_cond, tension_cond, neutr_cond, water_cond, oxid_cond, root):
    # Print oil analysis and recommendation
    
    # Create a new window
    res = Toplevel(root)
    res.configure(background="white")
    
    case_i = 0
    case_iii = 0
    
    
    # Frame design
    Label(res, text="ANALYSIS RESULTS", bg="white", font="Times 18 bold").grid(row=0, columnspan=4, sticky=S,  column=0)
    sep1 = ttk.Separator(res, orient='horizontal').grid(row=1, columnspan=5, sticky="ew", pady=5)

    
    # Print date
    year, month, day = gt.get_date()
    date_label = Label(res, text="Date: " + day + "/" + month + "/" + year, bg="white", font="Times 13 bold")
    date_label.grid(row=2, column=0, sticky=W)
    
    
    # Print clock
    hour, minute, second = gt.get_clock()
    clk_label = Label(res, text="Time: " + hour + ":" + minute + ":" + second, bg="white", font="Times 13 bold")
    clk_label.grid(row=3, column=0, sticky=W)
    
    
    # Print general information
    # Print serial number
    Label(res, text="Serial Number: " + serial_num, bg="white", font="Times 13 bold").grid(row=4, sticky=W, column=0)
    # Print insulation oil type
    Label(res, text="Insulation Material: " + oil, bg="white", font="Times 13 bold").grid(row=5, sticky=W, column=0)
    # Print transformer voltage
    Label(res, text="Voltage of a transformer [kV]: " + str(tx_v), bg="white", font="Times 13 bold").grid(row=6, sticky=W, column=0)
    # Draw a separation line
    sep2 = ttk.Separator(res, orient='horizontal').grid(row=7, columnspan=5, sticky="ew", pady=5)

    
    # Declare lists
    condition = [dbv_cond, water_cond, factor_cond, tension_cond, neutr_cond, oxid_cond]
    params = ["Dielectric breakdown voltage", "Dissipation Factor", "Interfacial_tension",
              "Neutralization number (acidity)", "Water content", "Oxidation inhibitor content"]
    
    # Print parameters' states
    Label(res, text="Parameters' states", bg="white", font = "Times 18 bold").grid(row=8, columnspan=4, sticky=S, column=0)
    
    # Print state for dielectric breakdown voltage
    if dbv_cond == "Satisfactory":
        res_dbv = StringVar()
        lbl_dbv_msg = Label(res, bg='green', textvariable=res_dbv, font="Times 14")
        res_dbv.set("Dielectric breakdown voltage is in satisfactory condition\n")
        lbl_dbv_msg.grid(row=9, sticky=W, column=0, columnspan=2)
    else:
        res_dbv = StringVar()
        lbl_dbv_msg = Label(res, bg='red', textvariable=res_dbv, font="Times 14")
        res_dbv.set("Dielectric breakdown voltage is not in  satisfactory condition\n")
        lbl_dbv_msg.grid(row=9, sticky=W, column=0, columnspan=2)
    
    # Print state for dissipation factor
    if factor_cond == "Satisfactory":
        res_df = StringVar()
        lbl_df_msg = Label(res, bg='green', textvariable=res_df, font="Times 14")
        res_df.set("Dissipation factor is in satisfactory condition\n")
        lbl_df_msg.grid(row=10, sticky=W, column=0, columnspan=2)
    else:
        res_df = StringVar()
        lbl_df_msg = Label(res, bg='red', textvariable=res_df, font="Times 14")
        res_df.set("Dissipation factor is not in satisfactory condition\n")
        lbl_df_msg.grid(row=10, sticky=W, column=0, columnspan=2)
    
    # Print state for interfacial tension
    if tension_cond == "Satisfactory":
        res_tens = StringVar()
        lbl_tens_msg = Label(res, bg='green', textvariable=res_tens, font="Times 14")
        res_tens.set("Interfacial tension is in satisfactory condition\n")
        lbl_tens_msg.grid(row=11, sticky=W, column=0, columnspan=2)
    else:
        res_tens = StringVar()
        lbl_tens_msg = Label(res, bg='red', textvariable=res_tens, font="Times 14")
        res_tens.set("Interfacial tension is not in satisfactory condition\n")
        lbl_tens_msg.grid(row=11, sticky=W, column=0, columnspan=2)

    # Print state for neutralization number
    if neutr_cond == "Satisfactory":
        res_neutr = StringVar()
        lbl_neutr_msg = Label(res, bg='green', textvariable=res_neutr, font="Times 14")
        res_neutr.set("Neutralization number is in satisfactory condition\n")
        lbl_neutr_msg.grid(row=12, sticky=W, column=0, columnspan=2)
    else:
        res_neutr = StringVar()
        lbl_neutr_msg = Label(res, bg='red', textvariable=res_neutr, font="Times 14")
        res_neutr.set("Neutralization number is not in satisfactory condition\n")
        lbl_neutr_msg.grid(row=12, sticky=W, column=0, columnspan=2)
    
    # Print state for water content
    if water_cond == "Satisfactory":
        res_water = StringVar()
        lbl_water_msg = Label(res, bg='green', textvariable=res_water, font="Times 14")
        res_water.set("Water content is in satisfactory condition\n")
        lbl_water_msg.grid(row=13, sticky=W, column=0, columnspan=2)
    else:
        res_water = StringVar()
        lbl_water_msg = Label(res, bg='red', textvariable=res_water, font="Times 14")
        res_water.set("Water content is not in satisfactory condition\n")
        lbl_water_msg.grid(row=13, sticky=W, column=0, columnspan=2)
    
    # Print state for oxidation inhibitor conten
    if oxid_cond == "Satisfactory":
        res_oxid = StringVar()
        lbl_oxid_msg = Label(res, bg='green', textvariable=res_oxid, font="Times 14")
        res_oxid.set("Oxidation inhibitor content is in satisfactory condition\n")
        lbl_oxid_msg.grid(row=14, sticky=W, column=0, columnspan=2)
    else:
        res_oxid = StringVar()
        lbl_oxid_msg = Label(res, bg='red', textvariable=res_oxid, font="Times 14")
        res_oxid.set("Oxidation inhibitor content is not in satisfactory condition\n")
        lbl_oxid_msg.grid(row=14, sticky=W, column=0, columnspan=2)


    # Draw a separating line
    sep3 = ttk.Separator(res, orient='horizontal').grid(row=15, columnspan=5, sticky="ew", pady=5)
    
    
    # Print recommendation
    Label(res, text="Recommendations: ", bg="white", font="Times 15 bold").grid(row=16, sticky=W, column=0)
    
    
    for i in range(len(condition)):
        if condition[i] == "Satisfactory":

            case_i += 1

        elif condition[i] == "Unsatisfactory":

            if i > 1:
                case_iii += 1
    
    # Check condition for class 1 mineral oil
    if case_i == 6:
        case_one = StringVar()
        lbl_case_one = Label(res, bg='green', textvariable=case_one, font="Times 14")
        case_one.set("Class I mineral oil \nMineral oil is in satisfactory condition.")
        lbl_case_one.grid(row=17, sticky=W, column=0)
    
    # Check condition for class 2 mineral oil
    elif case_iii > 0:
        case_three = StringVar()
        lbl_case_three = Label(res, bg='red', textvariable=case_three, font="Times 14")
        case_three.set(
            "Class III mineral oil \nMineral oil should be reclamed using Fuller's earth or an equivalent method.")
        lbl_case_three.grid(row=17, sticky=W, column=0)
    
    # Check condition for class 3 mineral oil
    else:
        case_two = StringVar()
        lbl_case_two = Label(res, bg='red', textvariable=case_two, font="Times 14")
        case_two.set(
            "Class II mineral oil \nMineral oil needs to be reprocesed by mechanical filtration such as filter pressing, vacuum dehydration or similar technique.")
        lbl_case_two.grid(row=17, sticky=W, column=0)
    




