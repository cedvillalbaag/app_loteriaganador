#Importar librerías
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from random import randint

#Crear ventana - Parametros basicos
root = Tk()
root.title("App - Ganador Aleatorio")
root.iconbitmap('img/basedatos.ico')
root.geometry("580x320")

topLabel = Label(root, text="Lotería Ganador", font=("Helvetica", 24), justify=CENTER)
topLabel.grid(row=0, column=0, columnspan=2)

#Crear Botones
def Borrar():
    winnerLabel.destroy()
    winButton['state']=NORMAL
    
def Pick():
    global winnerLabel
    entries = ["Carlos", "Jorge", "Alonso", "Alonso"] 
    #Lista de Postulados
    #Realizar una lista unica de los valores ingresados
    entries_set = set(entries)
    unique_entries = list(entries_set)
    #Obtener el numero de postulantes aplicados
    our_number = len(unique_entries)
    #Seleccionar un numero aleatorio
    rando = randint(0, our_number)
    winnerLabel=Label(root, text="Y el Ganador es: "+ unique_entries[rando], font=("Helvetica", 18), justify=CENTER, bg='yellow')
    winnerLabel.grid(row=3, column=0, pady=50, columnspan=2)
    winButton['state']=DISABLED

espacioLabel=Label(root, text="").grid(row=1, column=0)

winButton = Button(root, text="Seleccionar el Ganador", font=("Helvetica", 24), command=Pick)
winButton.grid(row=2,column=0, padx=10)

borrarButton = Button(root, text="Borrar", command=Borrar, font=("Helvetica", 24))
borrarButton.grid(row=2, column=1)

#Bucle infinito (Mantiene abierta la ventana/ aplicación)
root.mainloop()