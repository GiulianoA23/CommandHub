import tkinter as tk
import os

class Terminal:
    def __init__(self, master):
        self.master = master
        self.master.title("Terminal del Sistema")

        # Crear un área de texto para mostrar la salida
        self.text_area = tk.Text(self.master, wrap='word', height=20, width=50, bg='black', fg='white', insertbackground='white')
        self.text_area.pack(padx=10, pady=10)

        # Crear una entrada para recibir comandos
        self.entry = tk.Entry(self.master, bg='white', fg='black')
        self.entry.pack(padx=10, pady=5)
        self.entry.bind("<Return>", self.ejecutar_comando)
        self.entry.bind("<Tab>", self.autocompletar)  # Autocompletar al presionar Tab

        self.comandos = ['ls', 'pwd', 'cd', 'exit', 'edit', 'touch', 'rm', 'cat', 'help']  # Lista de comandos disponibles

    def ejecutar_comando(self, event):
        """Ejecuta el comando ingresado en la terminal."""
        comando = self.entry.get()
        self.entry.delete(0, tk.END)  # Limpiar la entrada

        resultado = self.procesar_comando(comando)
        self.text_area.insert(tk.END, f"$ {comando}\n{resultado}\n")  # Mostrar el comando y su resultado
        self.text_area.see(tk.END)  # Desplazar hacia abajo para ver el último resultado

    def autocompletar(self, event):
        """Autocompleta el comando o nombre de archivo."""
        texto_actual = self.entry.get()
        opciones = [cmd for cmd in self.comandos if cmd.startswith(texto_actual)]
        
        if len(opciones) == 1:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, opciones[0])  # Completar el comando
        elif len(opciones) > 1:
            # Muestra las opciones de autocompletado en el área de texto
            self.text_area.insert(tk.END, f"Opciones: {', '.join(opciones)}\n")
            self.text_area.see(tk.END)

        return "break"  # Evitar el sonido de error de la tecla Tab

    def procesar_comando(self, comando):
        """Procesa el comando ingresado y devuelve el resultado."""
        partes = comando.split()
        if not partes:
            return "Comando no reconocido."

        comando_principal = partes[0]

        if comando_principal == 'ls':
            return self.listar_directorio()
        elif comando_principal == 'pwd':
            return os.getcwd()
        elif comando_principal == 'cd':
            if len(partes) > 1:
                return self.cambiar_directorio(partes[1])
            else:
                return "Uso: cd <directorio>"
        elif comando_principal == 'touch':
            if len(partes) > 1:
                return self.crear_archivo(partes[1])
            else:
                return "Uso: touch <nombre_archivo>"
        elif comando_principal == 'rm':
            if len(partes) > 1:
                return self.eliminar_archivo(partes[1])
            else:
                return "Uso: rm <nombre_archivo>"
        elif comando_principal == 'cat':
            if len(partes) > 1:
                return self.mostrar_contenido_archivo(partes[1])
            else:
                return "Uso: cat <nombre_archivo>"
        elif comando_principal == 'help':
            return self.mostrar_ayuda()
        elif comando_principal == 'exit':
            self.master.quit()
            return "Saliendo..."
        else:
            return f"Comando no reconocido: {comando_principal}"

    def listar_directorio(self):
        """Lista los archivos en el directorio actual."""
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

    def crear_archivo(self, nombre_archivo):
        """Crea un archivo vacío con el nombre especificado."""
        try:
            with open(nombre_archivo, 'w') as f:
                pass
            return f"Archivo creado: {nombre_archivo}"
        except Exception as e:
            return f"Error al crear el archivo: {e}"

    def eliminar_archivo(self, nombre_archivo):
        """Elimina el archivo especificado."""
        try:
            os.remove(nombre_archivo)
            return f"Archivo eliminado: {nombre_archivo}"
        except FileNotFoundError:
            return f"Archivo no encontrado: {nombre_archivo}"
        except Exception as e:
            return f"Error al eliminar el archivo: {e}"

    def mostrar_contenido_archivo(self, nombre_archivo):
        """Muestra el contenido del archivo especificado."""
        try:
            with open(nombre_archivo, 'r') as f:
                contenido = f.read()
                return contenido
        except FileNotFoundError:
            return f"Archivo no encontrado: {nombre_archivo}"
        except Exception as e:
            return f"Error al leer el archivo: {e}"

    def mostrar_ayuda(self):
        """Muestra la lista de comandos disponibles."""
        ayuda = """
        Comandos disponibles:
        - ls          : Muestra el contenido del directorio actual.
        - pwd         : Muestra la ruta del directorio actual.
        - cd <dir>    : Cambia al directorio especificado.
        - touch <file>: Crea un archivo vacío con el nombre especificado.
        - rm <file>   : Elimina el archivo especificado.
        - cat <file>  : Muestra el contenido del archivo especificado.
        - help        : Muestra esta ayuda.
        - exit        : Sale del sistema.
        """
        return ayuda.strip()

def main():
    # Crear la ventana principal del terminal
    root = tk.Tk()
    terminal = Terminal(root)
    root.mainloop()

if __name__ == "__main__":
    main()
