import tkinter as tk
from tkinter import messagebox, filedialog
import os
import shutil

class GestorArchivos(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Gestor de Archivos")
        self.geometry("400x300")

        # Crear un marco para la lista de archivos
        self.frame = tk.Frame(self)
        self.frame.pack(pady=10)

        # Crear un área de lista para mostrar los archivos
        self.lista_archivos = tk.Listbox(self.frame, width=50, height=15)
        self.lista_archivos.pack(side=tk.LEFT, padx=5)

        # Crear un scrollbar
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.lista_archivos.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.lista_archivos.yview)

        # Botones para las operaciones de archivos
        self.boton_copiar = tk.Button(self, text="Copiar", command=self.copiar_archivo)
        self.boton_copiar.pack(pady=5)

        self.boton_mover = tk.Button(self, text="Mover", command=self.mover_archivo)
        self.boton_mover.pack(pady=5)

        self.boton_renombrar = tk.Button(self, text="Renombrar", command=self.renombrar_archivo)
        self.boton_renombrar.pack(pady=5)

        self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.eliminar_archivo)
        self.boton_eliminar.pack(pady=5)

        # Cargar archivos en la lista
        self.cargar_archivos()

    def cargar_archivos(self):
        """Carga los archivos del directorio actual en la lista."""
        self.lista_archivos.delete(0, tk.END)  # Limpiar la lista
        for archivo in os.listdir('.'):
            self.lista_archivos.insert(tk.END, archivo)  # Agregar archivo a la lista

    def copiar_archivo(self):
        """Copia el archivo seleccionado."""
        seleccion = self.lista_archivos.curselection()
        if seleccion:
            archivo = self.lista_archivos.get(seleccion)
            destino = filedialog.askdirectory()  # Seleccionar el directorio de destino
            if destino:
                shutil.copy(archivo, destino)
                messagebox.showinfo("Éxito", f"Archivo '{archivo}' copiado a '{destino}'")
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un archivo.")

    def mover_archivo(self):
        """Mueve el archivo seleccionado."""
        seleccion = self.lista_archivos.curselection()
        if seleccion:
            archivo = self.lista_archivos.get(seleccion)
            destino = filedialog.askdirectory()  # Seleccionar el directorio de destino
            if destino:
                shutil.move(archivo, destino)
                messagebox.showinfo("Éxito", f"Archivo '{archivo}' movido a '{destino}'")
                self.cargar_archivos()  # Actualizar la lista
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un archivo.")

    def renombrar_archivo(self):
        """Renombra el archivo seleccionado."""
        seleccion = self.lista_archivos.curselection()
        if seleccion:
            archivo_actual = self.lista_archivos.get(seleccion)
            nuevo_nombre = simpledialog.askstring("Renombrar", "Nuevo nombre:", initialvalue=archivo_actual)
            if nuevo_nombre:
                os.rename(archivo_actual, nuevo_nombre)
                messagebox.showinfo("Éxito", f"Archivo renombrado a '{nuevo_nombre}'")
                self.cargar_archivos()  # Actualizar la lista
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un archivo.")

    def eliminar_archivo(self):
        """Elimina el archivo seleccionado."""
        seleccion = self.lista_archivos.curselection()
        if seleccion:
            archivo = self.lista_archivos.get(seleccion)
            confirmacion = messagebox.askyesno("Confirmar", f"¿Estás seguro de que deseas eliminar '{archivo}'?")
            if confirmacion:
                os.remove(archivo)
                messagebox.showinfo("Éxito", f"Archivo '{archivo}' eliminado.")
                self.cargar_archivos()  # Actualizar la lista
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un archivo.")

def main():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    gestor = GestorArchivos(root)
    root.mainloop()

if __name__ == "__main__":
    main()
