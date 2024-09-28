#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 12:26:16 2024

@author: ricardo_aguilar
"""

import tkinter as tk
from tkinter import messagebox

# Creacion de contenedor principal
root = tk.Tk()

global resistor
resistor=0
global para_ser
para_ser=0



voltaje_ini=5;

# Nombre de la ventana del contenedor
root.title("Ventana de prueba")
root.resizable(True,True)

# Creacion del frame principal
miframe = tk.Frame(root, width=1200,height=600)
miframe.pack()

# Variables
resistencia_total= tk.StringVar()
CORRIENTE = tk.StringVar()
VOLTAJE = tk.StringVar()



# Num 1
label1 = tk.Label(miframe, text="Numero 1:")
label1.grid(row=0, column=0, sticky="e", padx=10, pady=10)
entry1 = tk.Entry(miframe)
entry1.grid(row=0, column=1, padx=10, pady=10)

# Num 2
label2 = tk.Label(miframe, text="Numero 2:")
label2.grid(row=1, column=0, sticky="e", padx=10, pady=10)
entry2 = tk.Entry(miframe)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Num 3
label3 = tk.Label(miframe, text="Numero 3:")
label3.grid(row=2, column=0, sticky="e", padx=10, pady=10)
entry3 = tk.Entry(miframe)
entry3.grid(row=2, column=1, padx=10, pady=10)

# Num 4
label4 = tk.Label(miframe, text="Numero 4:")
label4.grid(row=3, column=0, sticky="e", padx=10, pady=10)
entry4 = tk.Entry(miframe)
entry4.grid(row=3, column=1, padx=10, pady=10)

# Num 4
label5 = tk.Label(miframe, text="Numero 5:")
label5.grid(row=4, column=0, sticky="e", padx=10, pady=10)
entry5 = tk.Entry(miframe)
entry5.grid(row=4, column=1, padx=10, pady=10)



def resistencia_total_p():
    
    global para_ser
    para_ser=1
    
    try:
        
        # Obtener los valores de las entradas
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        num4 = float(entry4.get())
        num5 = float(entry5.get())
        
        resistencia_total.set(str(1/((1/num1)+(1/num2)+(1/num3)+(1/num4)+(1/num5))))
    
    except ValueError:
        # None
        messagebox.showerror("Error", "Por favor ingresa solo números.")

def resistencia_total_s():
    
    global para_ser
    para_ser=2
    
    
    try:
        
        # Obtener los valores de las entradas
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        num4 = float(entry4.get())
        num5 = float(entry5.get())
        
        resistencia_total.set(str((num1+num2+num3+num4+num5)))
    
    except ValueError:
        # None
        messagebox.showerror("Error", "Por favor ingresa solo números.")


def voltaje_p():
    try:
    
        
        VOLTAJE.set(str(5))
    
    except ValueError:
        # None
        messagebox.showerror("Error", "Por favor ingresa solo números.")


def voltaje_s():
    try:
        
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        num4 = float(entry4.get())
        num5 = float(entry5.get())
        if (resistor==0):
            VOLTAJE.set(str(0))
        
        elif (resistor==1):
            r1=num1
            r2=num2+num3+num4+num5
            VOLTAJE.set(str((voltaje_ini*r1)/(r1+r2)))
        
        elif (resistor==2):
            r1=num1+num2
            r2=num3+num4+num5
            VOLTAJE.set(str((voltaje_ini*r1)/(r1+r2)))
        
        elif (resistor==3):
            r1=num1+num2+num3
            r2=num4+num5
            VOLTAJE.set(str((voltaje_ini*r1)/(r1+r2)))
        
        elif (resistor==4):
            r1=num1+num2+num3+num4
            r2=num5
            VOLTAJE.set(str((voltaje_ini*r1)/(r1+r2)))
        
        elif (resistor==5):
            VOLTAJE.set(str(0))
    
    except ValueError:
        # None
        messagebox.showerror("Error", "Por favor ingresa solo números.")



def resistor1():
    global resistor
    resistor=1
    if (para_ser==1):
        voltaje_p()
    if (para_ser==2):
        voltaje_s()
        
    
def resistor2():
    global resistor
    resistor=2
    if (para_ser==1):
        voltaje_p()
    if (para_ser==2):
        voltaje_s()
    
def resistor3():
    global resistor
    resistor=3
    if (para_ser==1):
        voltaje_p()
    if (para_ser==2):
        voltaje_s()

def resistor4():
    global resistor
    resistor=4
    if (para_ser==1):
        voltaje_p()
    if (para_ser==2):
        voltaje_s()
    
def resistor5():
    global resistor
    resistor=5
    if (para_ser==1):
        voltaje_p()
    if (para_ser==2):
        voltaje_s()

       


# Boton suma
boton_1= tk.Button(miframe, text="V1/I1", width=10,command=resistor1)
boton_1.grid(row=0,column=2)

boton_2= tk.Button(miframe, text="V2/I2", width=10,command=resistor2)
boton_2.grid(row=1,column=2)

boton_3 = tk.Button(miframe, text="V3/I3", width=10,command=resistor3)
boton_3.grid(row=2,column=2)

boton_4 = tk.Button(miframe, text="V4/I4", width=10,command=resistor4)
boton_4.grid(row=3,column=2)

boton_4 = tk.Button(miframe, text="V5/I5", width=10,command=resistor5)
boton_4.grid(row=4,column=2)

boton_paralelo = tk.Button(miframe, text="PARALELO", width=10,command=resistencia_total_p)
boton_paralelo.grid(row=5,column=3)

boton_serie= tk.Button(miframe, text="SERIE", width=10, command=resistencia_total_s)
boton_serie.grid(row=6,column=3)



# Resultado
label6 = tk.Label(miframe, text="CORRIENTE:")
label6.grid(row=5, column=0, sticky="e", padx=10, pady=10)
entry6 = tk.Entry(miframe, textvariable=CORRIENTE, state='readonly')
entry6.grid(row=5, column=1, padx=0, pady=10)

label7 = tk.Label(miframe, text="VOLTAJE:")
label7.grid(row=6, column=0, sticky="e", padx=10, pady=10)
entry7 = tk.Entry(miframe, textvariable=VOLTAJE, state='readonly')
entry7.grid(row=6, column=1, padx=0, pady=10)

label8 = tk.Label(miframe, text="RESISTENCIA TOTAL:")
label8.grid(row=7, column=0, sticky="e", padx=10, pady=10)
entry8 = tk.Entry(miframe, textvariable=resistencia_total, state='readonly')
entry8.grid(row=7, column=1, padx=0, pady=10)

root.mainloop()