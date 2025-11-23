#impotar las librerias
import tkinter as tk
def mostrar_ventana2():
    ventana1.withdraw() # esta funcion sirve parta ocultar la ventana 1 
    ventana2.deiconify() # muestra la ventana 2
def regresar():
    ventana2.withdraw() # esta funcion sirve para que oculte la ventana 2
    ventana1.deiconify() # muestre la ventana 1

#creacion de ventana 1
ventana1= tk.Tk()
ventana1.config(bg="#A7F2ED")
label1=tk.Label(ventana1, text="Esta es la ventana numero 1")
ventana1.geometry("600x400")
label1.pack()
btn1=tk.Button(ventana1, text="ir ala ventana 2 ",command=mostrar_ventana2)
btn1.pack()


#creacion de ventana 2
ventana2= tk.Tk()
ventana2.config(bg="#4BDE7A")
label2=tk.Label(ventana2, text="Esta es la ventana numero 2")
ventana2.geometry("300x300")
label2.pack()
btn2=tk.Button(ventana2, text="ir ala ventana 1 ",command=regresar)
btn2.pack()
ventana2.withdraw()

#creacion de ventanas (lanzar la interfaz)
ventana1.mainloop()