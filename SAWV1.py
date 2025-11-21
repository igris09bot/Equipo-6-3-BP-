#importrar la  biblioteca 
import tkinter as tk 
from tkinter import ttk 

#crear ventana en Python 
ventana=tk.Tk()
#configuramos la ventana
ventana.title("esta es mi primera ventana")
ventana.geometry("800x700")
ventana.columnconfigure(0, weight=1)

#agregamos los widgets
ttk.Label(ventana,text="hola es mi primera interfaz grafica en python").grid(column=0,row=0)
ttk.Label(ventana, text="Equipo 6 - Materia: Metodología aguiles").grid(column=0, row=1)
ttk.Label(ventana, text="integrantesdel equipo").grid(column=0, row=2)
ttk.Label(ventana, text=" fernando hermenegildo martinez ").grid(column=0, row=3)
ttk.Label(ventana, text=" jaqueline asquino de la cruz ").grid(column=0, row=4)
ttk.Label(ventana, text=" Tu QUESOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTE ").grid(column=0, row=5)


#activamos la ventana
ventana.resizable(0,0)
ventana.mainloop()