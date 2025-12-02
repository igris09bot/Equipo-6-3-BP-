import tkinter as tk
from tkinter import ttk

# ---------- CONFIGURACIÓN DE COLORES Y FUENTE ----------
COLOR_FONDO = "#FFFFFF"
COLOR_MENU = "#F296FE"
COLOR_TEXTO = "#020202"
FUENTE_TITULO = ("Arial", 16, "bold")
FUENTE_TEXTO = ("Arial", 12)

# ---------- VENTANA PRINCIPAL ----------
root = tk.Tk()
root.title("Bienestar Total")
root.geometry("900x500")
root.config(bg=COLOR_FONDO)

# ---------- FRAME MENÚ LATERAL ----------
menu_frame = tk.Frame(root, bg=COLOR_MENU, width=200)
menu_frame.pack(side="left", fill="y")

# ---------- FRAME CONTENIDO ----------
contenido_frame = tk.Frame(root, bg=COLOR_FONDO)
contenido_frame.pack(side="right", fill="both", expand=True)

# ---------- FUNCIÓN PARA CAMBIAR DE PÁGINA ----------
def mostrar_pagina(nombre):
    # Eliminar todos los widgets del frame de contenido
    for widget in contenido_frame.winfo_children():
        widget.destroy()
    
    # Llamar a la función de la página correspondiente
    paginas[nombre]()

# ---------- PÁGINAS ----------
def pagina_bienvenida():
    tk.Label(contenido_frame, text="Bienvenido a Bienestar contra el ciber sexo", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=30)
    tk.Label(contenido_frame, text="El objetivo de Bienestar Digital es promover", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack(pady=10)

def pagina_registro():
    tk.Label(contenido_frame, text="Registro de Usuario", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    # Ejemplo de campo:
    tk.Label(contenido_frame, text="Nombre", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack(pady=5)
    tk.Entry(contenido_frame, width=40).pack(pady=5)
    # Nota: Los campos de 'Edad' y 'Correo' están en el código de la imagen
    # pero aquí solo incluí uno como ejemplo simplificado para la estructura.
    # En la imagen original están: for campo in ["Nombre", "Edad", "Correo"]:
    # tk.Label(contenido_frame, text=f"{campo}:", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack()
    # tk.Entry(contenido_frame, width=40).pack(pady=5)

def pagina_test():
    tk.Label(contenido_frame, text="Test de Bienestar", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    tk.Label(contenido_frame, text="Responde las siguientes preguntas para conocer tu nivel de bienestar.", wraplength=600, bg=COLOR_FONDO, font=FUENTE_TEXTO).pack(pady=10)
    ttk.Button(contenido_frame, text="Iniciar Test", command=lambda: print("Test Iniciado")).pack(pady=20)
    # Usé un print como placeholder para el comando del botón

# ---------- DICCIONARIO DE PÁGINAS ----------
paginas = {
    "Bienvenida": pagina_bienvenida,
    "Registro": pagina_registro,
    "Test": pagina_test,
}

# ---------- BOTONES DE MENÚ LATERAL ----------
for nombre in paginas:
    # El comando llama a mostrar_pagina() con el nombre de la página
    ttk.Button(menu_frame, text=nombre, command=lambda n=nombre: mostrar_pagina(n)).pack(fill="x", pady=5, padx=10)

# Botón de Salir
ttk.Button(menu_frame, text="Salir", command=root.quit).pack(side="bottom", pady=10)

# ---------- MOSTRAR PÁGINA INICIAL ----------
pagina_bienvenida()

# Iniciar el bucle principal de Tkinter
root.mainloop()