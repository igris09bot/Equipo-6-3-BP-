import tkinter as tk
from tkinter import ttk

# Colores y fuentes
COLOR_FONDO = "#A7F2ED"
COLOR_MENU = "#75E69A"
COLOR_TEXTO = "#FFFFFF"
FUENTE_TEXTO = ("Arial", 16, "bold")
FUENTE_TITULO = ("Arial", 12)

# Funciones de navegación
def ir_a(pagina_actual, pagina_siguiente):
    pagina_actual.withdraw()
    pagina_siguiente.deiconify()

def regresar(pagina_actual, pagina_anterior):
    pagina_actual.withdraw()
    pagina_anterior.deiconify()

# Ventana principal
ventanaini = tk.Tk()
ventanaini.title("1-VENTANA DE BIENVENIDA")
ventanaini.geometry("800x600")

tk.Label(ventanaini, text="Bienvenido al software de detección de adicción al cibersexo").pack(pady=10)
tk.Label(ventanaini, text="El objetivo de Bienestar Digital es promover el autocuidado, la reflexión y el acceso a herramientas que ayuden a tomar decisiones conscientes sobre la vida sexual en entornos digitales.").pack(pady=10)
btn1 = tk.Button(ventanaini, text="Iniciar", command=lambda: ir_a(ventanaini, ventanaregis))
btn1.pack(pady=30)

# Ventana de registro
ventanaregis = tk.Toplevel(ventanaini)
ventanaregis.title("2-VENTANA DE REGISTRO")
ventanaregis.geometry("800x400")

tk.Label(ventanaregis, text="Registro de Usuario").pack(pady=20)
tk.Label(ventanaregis, text="Nombre:").pack()
tk.Entry(ventanaregis).pack()
tk.Label(ventanaregis, text="Edad:").pack()
tk.Entry(ventanaregis).pack()
tk.Label(ventanaregis, text="Correo electrónico:").pack()
tk.Entry(ventanaregis).pack()

tk.Button(ventanaregis, text="Regresar", command=lambda: regresar(ventanaregis, ventanaini)).pack(side="left", padx=50, pady=40)
tk.Button(ventanaregis, text="Continuar", command=lambda: ir_a(ventanaregis, ventanatest)).pack(side="right", padx=50, pady=40)

# Ventana de test
ventanatest = tk.Toplevel(ventanaini)
ventanatest.title("3-VENTANA DE TEST")
ventanatest.geometry("800x400")

tk.Label(ventanatest, text="Esta es la ventana donde se incluirá el test para adicciones").pack(pady=20)
tk.Label(ventanatest, text="Responde las siguientes preguntas", wraplength=400).pack(pady=20)

tk.Button(ventanatest, text="Regresar", command=lambda: regresar(ventanatest, ventanaregis)).pack(side="left", padx=50, pady=40)
tk.Button(ventanatest, text="Continuar", command=lambda: ir_a(ventanatest, ventanaresul)).pack(side="right", padx=50, pady=40)

# Ventana de resultados
ventanaresul = tk.Toplevel(ventanaini)
ventanaresul.title("4-VENTANA DE RESULTADO")
ventanaresul.geometry("800x400")
tk.Label(ventanaresul, text="Aquí se mostrarán los resultados del test").pack(pady=20)

# Ocultar ventanas secundarias al inicio
for v in (ventanaregis, ventanatest, ventanaresul):
    v.withdraw()

# Ejecutar la aplicación
ventanaini.mainloop()
