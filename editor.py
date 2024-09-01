import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename, asksaveasfilename

class Editor(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Editor de Texto")

        # Crear el área de texto desplazable
        self.text_area = ScrolledText(self, width=80, height=25, font=("Courier", 12))
        self.text_area.pack(padx=10, pady=10)

        # Crear la barra de menús
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)

        # Menú Archivo
        archivo_menu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="Archivo", menu=archivo_menu)
        archivo_menu.add_command(label="Abrir", command=self.abrir_archivo)
        archivo_menu.add_command(label="Guardar", command=self.guardar_archivo)
        archivo_menu.add_command(label="Guardar Como...", command=self.guardar_como)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.destroy)

        # Menú Editar
        editar_menu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="Editar", menu=editar_menu)
        editar_menu.add_command(label="Buscar", command=self.buscar)
        editar_menu.add_command(label="Reemplazar", command=self.reemplazar)

        # Menú Formato
        formato_menu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="Formato", menu=formato_menu)
        formato_menu.add_command(label="Resaltar Sintaxis", command=self.resaltar_sintaxis)

        self.filename = None

    def abrir_archivo(self):
        """Abre un archivo existente."""
        self.filename = askopenfilename(defaultextension=".txt", filetypes=[("Archivos de Texto", "*.txt"), ("Todos los Archivos", "*.*")])
        if self.filename:
            with open(self.filename, "r") as file:
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, file.read())

    def guardar_archivo(self):
        """Guarda el archivo actual."""
        if not self.filename:
            self.guardar_como()
        else:
            with open(self.filename, "w") as file:
                file.write(self.text_area.get("1.0", tk.END))

    def guardar_como(self):
        """Guarda el archivo con un nombre diferente."""
        self.filename = asksaveasfilename(initialfile="Sin Título.txt", defaultextension=".txt", filetypes=[("Archivos de Texto", "*.txt"), ("Todos los Archivos", "*.*")])
        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.text_area.get("1.0", tk.END))

    def buscar(self):
        """Muestra un cuadro de diálogo para buscar texto."""
        buscar_dialog = tk.Toplevel(self)
        buscar_dialog.title("Buscar")

        label = tk.Label(buscar_dialog, text="Buscar:")
        label.pack(padx=5, pady=5)

        self.buscar_entry = ttk.Entry(buscar_dialog)
        self.buscar_entry.pack(padx=5, pady=5)

        buscar_button = ttk.Button(buscar_dialog, text="Buscar", command=lambda: self.resaltar_texto(self.buscar_entry.get()))
        buscar_button.pack(padx=5, pady=5)

    def reemplazar(self):
        """Muestra un cuadro de diálogo para reemplazar texto."""
        reemplazar_dialog = tk.Toplevel(self)
        reemplazar_dialog.title("Reemplazar")

        label1 = tk.Label(reemplazar_dialog, text="Buscar:")
        label1.pack(padx=5, pady=5)

        self.buscar_entry = ttk.Entry(reemplazar_dialog)
        self.buscar_entry.pack(padx=5, pady=5)

        label2 = tk.Label(reemplazar_dialog, text="Reemplazar con:")
        label2.pack(padx=5, pady=5)

        self.reemplazar_entry = ttk.Entry(reemplazar_dialog)
        self.reemplazar_entry.pack(padx=5, pady=5)

        reemplazar_button = ttk.Button(reemplazar_dialog, text="Reemplazar", command=lambda: self.reemplazar_texto(self.buscar_entry.get(), self.reemplazar_entry.get()))
        reemplazar_button.pack(padx=5, pady=5)

    def resaltar_sintaxis(self):
        """Resalta la sintaxis del texto."""
        # Aquí puedes agregar la lógica para resaltar la sintaxis según el lenguaje de programación
        pass

    def resaltar_texto(self, texto):
        """Resalta todas las ocurrencias del texto especificado."""
        self.text_area.tag_remove("resaltado", "1.0", tk.END)
        start = "1.0"
        while True:
            start = self.text_area.search(texto, start, stopindex=tk.END)
            if not start:
                break
            end = f"{start}+{len(texto)}c"
            self.text_area.tag_add("resaltado", start, end)
            start = end
        self.text_area.tag_config("resaltado", background="yellow", foreground="black")

    def reemplazar_texto(self, buscar, reemplazar):
        """Reemplaza todas las ocurrencias del texto especificado."""
        self.text_area.replace("1.0", tk.END, self.text_area.get("1.0", tk.END).replace(buscar, reemplazar))

def main():
    root = tk.Tk()
    editor = Editor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
