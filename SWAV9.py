import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QTabWidget, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QRadioButton, QButtonGroup
from PyQt5.QtCore import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from Pregunta import Pregunta

class Bienvenida(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bienvenido")
        self.setGeometry(150, 100, 500, 300)

        layout = QVBoxLayout()

        lbl_titulo = QLabel("Bienvenido a la aplicación de Bienestar Digital")
        lbl_titulo.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50;")
        lbl_titulo.setAlignment(Qt.AlignCenter)

        lbl_texto = QLabel("Aquí podrás registrarte, realizar un test y ver tus resultados.\n\nHaz clic en continuar para empezar.")
        lbl_texto.setWordWrap(True)
        lbl_texto.setAlignment(Qt.AlignCenter)

        btn_continuar = QPushButton("Continuar")
        btn_continuar.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1c5980;
            }
        """)
        btn_continuar.clicked.connect(self.abrirPrincipal)

        layout.addWidget(lbl_titulo)
        layout.addWidget(lbl_texto)
        layout.addWidget(btn_continuar)

        self.setLayout(layout)

    def abrirPrincipal(self):
        self.close()
        self.principal = Principal()
        self.principal.show()

class Principal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("menu")
        self.setGeometry(100, 100, 600, 400)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.tab_registro = QWidget()
        self.tab_test = QWidget()
        self.tab_res = QWidget()
        self.tab_sintomas = QWidget()
        self.tab_ayuda = QWidget()
        self.tab_salir = QWidget()

        self.tabs.addTab(self.tab_registro, "Registro")
        self.tabs.addTab(self.tab_test, "Test")
        self.tabs.addTab(self.tab_res, "Resultados")
        self.tabs.addTab(self.tab_sintomas, "Síntomas")
        self.tabs.addTab(self.tab_ayuda, "Ayuda")
        self.tabs.addTab(self.tab_salir, "Salir")

        self.crear_pestana_registro()
        self.crear_pestana_test()
        self.crear_pestana_resultados()
        self.crear_pestana_sintomas()
        self.crear_pestana_ayuda()
        self.crear_pestana_salir()

    def crear_pestana_registro(self):
        layout = QVBoxLayout()

        titulo = QLabel("Crear Cuenta")
        titulo.setStyleSheet("font-weight: bold; font-size: 16px; color: #2c3e50;")
        layout.addWidget(titulo)

        self.input_nombre = QLineEdit()
        self.input_correo = QLineEdit()
        self.input_contra = QLineEdit()
        self.input_contra.setEchoMode(QLineEdit.Password)

        layout.addWidget(QLabel("Nombre:"))
        layout.addWidget(self.input_nombre)
        layout.addWidget(QLabel("Correo:"))
        layout.addWidget(self.input_correo)
        layout.addWidget(QLabel("Contraseña:"))
        layout.addWidget(self.input_contra)

        btn_registrar = QPushButton("Registrar")
        btn_registrar.clicked.connect(self.registrar_usuario)

        btn_registrar.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1c5980;
            }
        """)

        layout.addWidget(btn_registrar)
        self.tab_registro.setLayout(layout)

    def registrar_usuario(self):
        correo = self.input_correo.text()
        contra = self.input_contra.text()

        if correo == "" or contra == "":
            QMessageBox.warning(self, "Error", "Completa todos los campos")
        else:
            QMessageBox.information(self, "Éxito", "Cuenta creada correctamente")

    def crear_pestana_test(self):
        layout = QGridLayout()

        self.crearCuestionario()
        self.index = 0
        self.maximo = len(self.cuestionario)
        self.puntaje_total = 0

        self.lb_num = QLabel("")
        self.lb_pregunta = QLabel("")
        self.lb_pregunta.setWordWrap(True)

        radio_style = """
        QRadioButton {
            color: #2c3e50;
            font-weight: bold;
            spacing: 8px;
        }
        QRadioButton::indicator {
            width: 18px;
            height: 18px;
            border-radius: 9px;
            border: 2px solid #3498db;
            background-color: white;
        }
        QRadioButton::indicator:checked {
            background-color: #3498db;
            border: 2px solid #2980b9;
        }
        QRadioButton::indicator:hover {
            border: 2px solid #1abc9c;
        }
        """

        self.opcion_siempre = QRadioButton("Siempre")
        self.opcion_frecuente = QRadioButton("Frecuentemente")
        self.opcion_aveces = QRadioButton("A veces")
        self.opcion_nunca = QRadioButton("Nunca")

        for btn in [self.opcion_siempre, self.opcion_frecuente, self.opcion_aveces, self.opcion_nunca]:
            btn.setStyleSheet(radio_style)

        self.grupo_opciones = QButtonGroup()
        self.grupo_opciones.addButton(self.opcion_siempre)
        self.grupo_opciones.addButton(self.opcion_frecuente)
        self.grupo_opciones.addButton(self.opcion_aveces)
        self.grupo_opciones.addButton(self.opcion_nunca)

        self.btn_siguiente = QPushButton("Siguiente")
        self.btn_siguiente.clicked.connect(self.siguiente)

        self.btn_siguiente.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
            QPushButton:pressed {
                background-color: #1e8449;
            }
        """)

        layout.addWidget(self.lb_num, 0, 0)
        layout.addWidget(self.lb_pregunta, 1, 0)
        layout.addWidget(self.opcion_siempre, 2, 0)
        layout.addWidget(self.opcion_frecuente, 3, 0)
        layout.addWidget(self.opcion_aveces, 4, 0)
        layout.addWidget(self.opcion_nunca, 5, 0)
        layout.addWidget(self.btn_siguiente, 6, 0)

        self.tab_test.setLayout(layout)
        self.mostrarPregunta()

    def crearCuestionario(self):
        self.cuestionario = [
            Pregunta(1,"¿Con qué frecuencia usas contenido sexual en línea para escapar del estrés o la tristeza?", 0),
            Pregunta(2,"¿Has intentado reducir el tiempo que pasas en actividades sexuales online sin éxito?", 0),
            Pregunta(3,"¿Sientes culpa o vergüenza después de consumir contenido pornográfico?",0),
            Pregunta(4,"¿Has dejado de realizar actividades sociales o familiares por estar en línea viendo contenido sexual?",0),
            Pregunta(5,"¿Tu consumo de cibersexo ha afectado negativamente tu relación de pareja?",0),
            Pregunta(6,"¿Has perdido interés en el sexo real debido al uso excesivo de contenido sexual digital?",0),
            Pregunta(7,"¿Ocultas tu actividad sexual en línea a familiares o amigos?",0),
            Pregunta(8,"¿Has llegado tarde o faltado al trabajo por estar viendo contenido sexual en línea?",0),
            Pregunta(9,"¿Sientes ansiedad o irritabilidad cuando no puedes acceder a contenido sexual digital?",0),
            Pregunta(10,"¿Has gastado dinero en exceso en servicios o suscripciones de contenido sexual?",0),
        ]

    def mostrarPregunta(self):
        self.grupo_opciones.setExclusive(False)
        for btn in [self.opcion_siempre, self.opcion_frecuente, self.opcion_aveces, self.opcion_nunca]:
            btn.setChecked(False)
        self.grupo_opciones.setExclusive(True)

        pregunta = self.cuestionario[self.index]
        self.lb_num.setText(f"Pregunta {pregunta.num_pregunta}")
        self.lb_pregunta.setText(pregunta.texto)

    def obtenerPuntajeOpcion(self):
        if self.opcion_siempre.isChecked(): return 3
        if self.opcion_frecuente.isChecked(): return 2
        if self.opcion_aveces.isChecked(): return 1
        if self.opcion_nunca.isChecked(): return 0
        return None

    def siguiente(self):
        puntaje = self.obtenerPuntajeOpcion()

        if puntaje is None:
            QMessageBox.warning(self, "Advertencia", "Debes seleccionar una opción antes de continuar.")
            return

        self.cuestionario[self.index].puntaje = puntaje
        self.puntaje_total += puntaje

        if self.index < self.maximo - 1:
            self.index += 1
            self.mostrarPregunta()
        else:
            self.finalizarTest()

    def finalizarTest(self):
        QMessageBox.information(self,"Resultado",f"Has finalizado el test.\n\nTu puntuación total es: {self.puntaje_total} puntos.")

        self.tabs.setCurrentWidget(self.tab_res)
        self.actualizarGrafica()

    def crear_pestana_resultados(self):
        layout = QVBoxLayout()
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)
        self.tab_res.setLayout(layout)

    def actualizarGrafica(self):
        self.fig.clear()
        ax = self.fig.add_subplot(111)

        preguntas = [f"P{p.num_pregunta}" for p in self.cuestionario]
        puntajes = [p.puntaje for p in self.cuestionario]

        colores = ["#3498db", "#2ecc71", "#e67e22", "#9b59b6", "#f39c12","#1abc9c", "#8e44ad", "#c0392b", "#16a085", "#2c3e50"]

        barras = ax.bar(preguntas, puntajes, color=colores)
        ax.set_ylim(0, 3)
        ax.set_title("Puntaje por pregunta")
        ax.set_ylabel("Puntaje")
        ax.set_xlabel("Preguntas")
        ax.grid(axis='y', linestyle='--', alpha=0.4)
        self.canvas.draw()

    def crear_pestana_sintomas(self):
        layout = QVBoxLayout()

        titulo = QLabel("Síntomas relacionados")
        titulo.setStyleSheet("font-weight: bold; font-size: 16px; color: #2c3e50;")
        layout.addWidget(titulo)

        texto = QLabel("Algunos síntomas comunes que pueden estar asociados al uso excesivo de contenido digital:\n\n""- Ansiedad o irritabilidad\n""- Aislamiento social\n""- Problemas de concentración\n""- Alteraciones del sueño\n""- Sentimientos de culpa o vergüenza\n")
        texto.setWordWrap(True)
        layout.addWidget(texto)

        btn_info = QPushButton("Más información")
        btn_info.setStyleSheet("""
            QPushButton {
                background-color: #e67e22;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #d35400;
            }
            QPushButton:pressed {
                background-color: #a84300;
                                           }
        """)
        btn_info.clicked.connect(lambda: QMessageBox.information(
            self, "Síntomas", "Consulta con un profesional si estos síntomas afectan tu vida diaria.")
        )

        layout.addWidget(btn_info)
        self.tab_sintomas.setLayout(layout)

    def crear_pestana_ayuda(self):
        layout = QVBoxLayout()
        titulo = QLabel("Opciones de ayuda")
        titulo.setStyleSheet("font-weight: bold; font-size: 16px; color: #2c3e50;")
        layout.addWidget(titulo)
        btn_profesional = QPushButton("Hablar con un psicólogo")
        btn_profesional.setStyleSheet("background-color: #3498db; color: white; font-weight: bold;")
        btn_profesional.clicked.connect(lambda: QMessageBox.information(self,"Profesional","Puedes comunicarte con un psicólogo al número: +52 222 123 4567"))
        
        layout.addWidget(btn_profesional)
        
        btn_video = QPushButton("Ver un video motivacional")
        btn_video.setStyleSheet("background-color: #2ecc71; color: white; font-weight: bold;")
        btn_video.clicked.connect(lambda: webbrowser.open("https://www.youtube.com/watch?v=mgmVOuLgFB0"))
        layout.addWidget(btn_video)
        
        btn_aliento = QPushButton("Recibir palabras de aliento")
        btn_aliento.setStyleSheet("background-color: #e67e22; color: white; font-weight: bold;")
        btn_aliento.clicked.connect(lambda: QMessageBox.information(self,"Aliento","Recuerda: cada paso que das hacia tu bienestar cuenta. ¡Tú puedes lograrlo!"))
        layout.addWidget(btn_aliento)
        self.tab_ayuda.setLayout(layout)

    def crear_pestana_salir(self):
        layout = QVBoxLayout()

        lbl = QLabel("¿Deseas cerrar la aplicación?")
        lbl.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl)

        btn_salir = QPushButton("Salir")
        btn_salir.setStyleSheet("background-color: #c0392b; color: white; font-weight: bold;")
        btn_salir.clicked.connect(QApplication.instance().quit)  # Cierra la aplicación
        layout.addWidget(btn_salir)

        self.tab_salir.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    bienvenida = Bienvenida()
    bienvenida.show()
    app.exec()