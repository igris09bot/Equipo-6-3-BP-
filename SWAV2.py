import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

#
# funcion que se ejecutacionar
#
def iniciar_test():
    messagebox.showinfo("inicio del test", "bienvenito al test de adicciones. \n\nPresiona OK para continuar")
    ventanaprin.destroy() # cierre la pantalla de bienvenida (puedes cambiarlo por abrir otra ventana)


#
# configurar la ventana principal
#
ventanaprin = tk.Tk()
ventanaprin.title("IU Bienvenida")
ventanaprin.config(bg= "#8EDBFF")


# configuracion posicion de la pantalla
ancho_pantalla = ventanaprin.winfo_screenwidth()
alto_pantalla = ventanaprin.winfo_screenheight()
# Se corrige la geometría de la ventana y el formato del f-string
ANCHO_VENTANA = 700
ALTO_VENTANA = 450
x = (ancho_pantalla // 2) - (ANCHO_VENTANA // 2)
y = (alto_pantalla // 2) - (ALTO_VENTANA // 2)
# Corrección: El formato f-string debe encerrar las variables x e y entre {}
ventanaprin.geometry(f"{ANCHO_VENTANA}x{ALTO_VENTANA}+{x}+{y}")

#
# Elementos graficos
#

# titulo principal
titulo = tk.Label(
    ventanaprin,
    text="BIENVENIDO A MI SOFTWARE PARA EL CIBER SEXO",
    # CORRECCIÓN: Se añade la coma faltante después del argumento 'text'
    font=("Arial", 18, "bold"),
    # CORRECCIÓN: Se añade la coma faltante después del argumento 'font'
    # Corrección de la abreviatura 'br' por 'bg' para color de fondo
    bg= "#8EFF31",
    # CORRECCIÓN: Se añade la coma faltante después del argumento 'bg'
    fg= "#000000",
    # CORRECCIÓN: Se añade la coma faltante después del argumento 'fg'
    wraplength= 550,
    justify= "center"
    # No es necesaria coma después del último argumento
)
titulo.pack(pady=30)

# insertar una imagen
try:
    # Nota: Asegúrate de que el archivo "OIP.png" exista en el mismo directorio
    imagen = PhotoImage(file="OIP.png")
    # CORRECCIÓN: Se corrigió la asignación de la imagen al Label: 'imagen' debe ser 'image'
    img_label = tk.Label(ventanaprin, image=imagen, bg= "#28C9C2")
    img_label.pack(pady=10)
except Exception:
    aviso = tk.Label(ventanaprin, text="no se encontro la imagen", bg= "#28C9C2", fg= "gray")
    aviso.pack()
    
# texto descriptivo
texto = tk.Label(
    ventanaprin,
    # CORRECCIÓN: La tupla debe cerrarse correctamente. Se añade el texto descriptivo dentro de 'text'
    text=(
         "Este test tiene como objetivo detectar posibles indicadores de adicción al cibersexo."
    ),
    # CORRECCIÓN: Se añade la coma faltante después del argumento 'text'
    font= ("Arial", 12),
    # CORRECCIÓN: Se añade la coma faltante después del argumento 'font'
    bg="#8EFF31",
    # CORRECCIÓN: Se añade la coma faltante después del argumento 'bg'
    fg="#000000",
    # CORRECCIÓN: Se añade la coma faltante después del argumento 'fg'
    wraplength=500,
    justify="center",
)
texto.pack(pady=20)

# elemento boton para iniciar el test
boton_iniciar = tk.Button(
    ventanaprin,
    text="Inicio TEST",
    font=("Arial", 14, "bold"),
    bg= "#141212",
    fg="white",
    relief="raised",
    bd=3,
    padx=20,
    pady=10,
    command= iniciar_test
)
boton_iniciar.pack(pady=20)

# ejecutar la interfaz de ventana
ventanaprin.mainloop()