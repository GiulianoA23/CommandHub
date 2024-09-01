import tkinter as tk
import os
import threading
from tkinter import filedialog
from PIL import Image, ImageTk  # Importar Pillow para manejar imágenes
from editor import Editor  # Asegúrate de que el archivo editor.py esté en el mismo directorio
from terminal import Terminal  # Asegúrate de que el archivo terminal.py esté en el mismo directorio
from gestor_archivos import GestorArchivos  # Asegúrate de que el archivo gestor_archivos.py esté en el mismo directorio

class Tema:
    def __init__(self, nombre, configuracion):
        self.nombre = nombre
        self.configuracion = configuracion

class AplicacionGrafica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Gráfico y de Comandos")

        # Crear un lienzo para dibujar
        self.canvas = tk.Canvas(self, width=800, height=600, bg='lightgray')
        self.canvas.pack()

        # Crear una barra de tareas en la parte inferior
        self.barra_tareas = tk.Frame(self, bg='lightblue', height=50)
        self.barra_tareas.pack(side=tk.BOTTOM, fill=tk.X)

        # Crear un menú para seleccionar el tema
        self.tema_var = tk.StringVar(value="Claro")  # Tema por defecto
        self.menu_tema = tk.OptionMenu(self.barra_tareas, self.tema_var, *[tema.nombre for tema in temas], command=lambda _: self.cambiar_tema())
        self.menu_tema.pack(side=tk.LEFT, padx=10, pady=10)

        # Crear un botón para establecer wallpaper
        self.boton_wallpaper = tk.Button(self.barra_tareas, text="Establecer Wallpaper", command=self.establecer_wallpaper)
        self.boton_wallpaper.pack(side=tk.LEFT, padx=10, pady=10)

        # Crear accesos directos en la barra de tareas
        self.boton_terminal = tk.Button(self.barra_tareas, text="Abrir Terminal", command=self.abrir_terminal)
        self.boton_terminal.pack(side=tk.LEFT, padx=10, pady=10)

        self.boton_editor = tk.Button(self.barra_tareas, text="Abrir Editor", command=self.abrir_editor)
        self.boton_editor.pack(side=tk.LEFT, padx=10, pady=10)

        self.boton_gestor_archivos = tk.Button(self.barra_tareas, text="Gestor de Archivos", command=self.abrir_gestor_archivos)
        self.boton_gestor_archivos.pack(side=tk.LEFT, padx=10, pady=10)

        self.boton_cerrar = tk.Button(self.barra_tareas, text="Cerrar Sistema", command=self.cerrar_sistema)
        self.boton_cerrar.pack(side=tk.RIGHT, padx=10, pady=10)

        # Vincular el evento de movimiento del mouse a la función dibujar_cuadrado
        self.canvas.bind("<Motion>", self.dibujar_cuadrado)
        self.canvas.bind("<Button-3>", self.recargar_sistema)

        # Iniciar el hilo para manejar comandos
        threading.Thread(target=self.manejar_comando, daemon=True).start()

        # Label para el wallpaper
        self.wallpaper_label = None

    def dibujar_cuadrado(self, event):
        """Dibuja un cuadrado blanco en la posición actual del mouse sin dejar rastros."""
        self.canvas.delete("all")
        x = event.x
        y = event.y
        tamaño = 50  # Tamaño del cuadrado
        self.canvas.create_rectangle(x, y, x + tamaño, y + tamaño, fill='white', outline='black')

    def recargar_sistema(self, event):
        """Recarga el sistema al hacer clic derecho."""
        print("Recargando el sistema...")
        self.canvas.delete("all")

    def manejar_comando(self):
        """Maneja la entrada de comandos desde la consola."""
        while True:
            comando = input("$ ")
            resultado = self.ejecutar_comando(comando)
            print(resultado)

    def ejecutar_comando(self, comando):
        """Ejecuta un comando ingresado por el usuario."""
        partes = comando.split()
        if not partes:
            return "Comando no reconocido."

        comando_principal = partes[0]

        if comando_principal == 'ls':
            return self.mostrar_directorio()
        elif comando_principal == 'pwd':
            return os.getcwd()
        elif comando_principal == 'cd':
            if len(partes) > 1:
                return self.cambiar_directorio(partes[1])
            else:
                return "Uso: cd <directorio>"
        elif comando_principal == 'edit':
            if len(partes) > 1:
                self.abrir_editor(partes[1])
                return f"Abriendo el editor para {partes[1]}"
            else:
                return "Uso: edit <nombre_archivo>"
        elif comando_principal == 'exit':
            print("Saliendo del sistema...")
            self.quit()
            return "Saliendo..."
        else:
            return f"Comando no reconocido: {comando_principal}"

    def mostrar_directorio(self):
        """Muestra el contenido del directorio actual."""
        try:
            archivos = os.listdir('.')
            return '\n'.join(archivos)
        except Exception as e:
            return f"Error al listar el directorio: {e}"

    def cambiar_directorio(self, directorio):
        """Cambia al directorio especificado."""
        try:
            os.chdir(directorio)
            return f"Cambiado al directorio: {directorio}"
        except FileNotFoundError:
            return f"Directorio no encontrado: {directorio}"
        except Exception as e:
            return f"Error al cambiar de directorio: {e}"

    def abrir_terminal(self):
        """Abre la ventana del terminal."""
        terminal_window = tk.Toplevel(self)
        Terminal(terminal_window)  # Crear una instancia de Terminal

    def abrir_editor(self, nombre_archivo=None):
        """Abre el editor de texto."""
        editor_window = tk.Toplevel(self)
        Editor(editor_window)  # Crear una instancia de Editor

    def abrir_gestor_archivos(self):
        """Abre el gestor de archivos."""
        gestor_window = tk.Toplevel(self)
        GestorArchivos(gestor_window)  # Crear una instancia de GestorArchivos

    def cerrar_sistema(self):
        """Cierra el sistema."""
        print("Saliendo del sistema...")
        self.quit()

    def cambiar_tema(self):
        """Cambia el tema de la aplicación."""
        tema_seleccionado = self.tema_var.get()
        tema = next((t for t in temas if t.nombre == tema_seleccionado), None)
        if tema:
            self.aplicar_tema(tema.configuracion)

    def aplicar_tema(self, configuracion):
        """Aplica el tema seleccionado a la aplicación."""
        for widget in self.winfo_children():
            widget.configure(bg=configuracion["bg"], fg=configuracion["fg"])
        
        self.canvas.configure(bg=configuracion["canvas_bg"])
        
        # Aplicar tema a los botones
        for widget in self.barra_tareas.winfo_children():
            widget.configure(bg=configuracion["button_bg"], fg=configuracion["button_fg"])

    def establecer_wallpaper(self):
        """Permite al usuario seleccionar un wallpaper."""
        wallpaper_path = filedialog.askopenfilename(title="Seleccionar Wallpaper", filetypes=[("Archivos de Imagen", "*.png;*.jpg;*.jpeg;*.bmp")])
        if wallpaper_path:
            # Cargar la imagen y establecerla como fondo
            img = Image.open(wallpaper_path)
            img = img.resize((800, 600))  # Redimensionar la imagen para que se ajuste a la ventana
            wallpaper = ImageTk.PhotoImage(img)
            
            # Si ya hay un wallpaper, lo eliminamos
            if self.wallpaper_label:
                self.wallpaper_label.destroy()

            # Crear un label para mostrar la imagen de fondo
            self.wallpaper_label = tk.Label(self, image=wallpaper)
            self.wallpaper_label.image = wallpaper  # Mantener una referencia de la imagen
            self.wallpaper_label.place(x=0, y=0, relwidth=1, relheight=1)  # Colocar la imagen en el fondo

# Definición de temas
temas = [
    Tema("Claro", {
        "bg": "white",
        "fg": "black",
        "canvas_bg": "lightgray",
        "button_bg": "lightblue",
        "button_fg": "black"
    }),
    Tema("Oscuro", {
        "bg": "black",
        "fg": "white",
        "canvas_bg": "gray",
        "button_bg": "darkgray",
        "button_fg": "white"
    })
]

def main():
    app = AplicacionGrafica()
    app.mainloop()

if __name__ == "__main__":
    main()
