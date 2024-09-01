import tkinter as tk
from tkinter import messagebox

class GestorVentanas(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Gestor de Ventanas")
        self.geometry("300x200")

        self.ventanas = []  # Lista para almacenar las ventanas abiertas

        # Crear un marco para la lista de ventanas
        self.frame = tk.Frame(self)
        self.frame.pack(pady=10)

        # Crear un área de lista para mostrar las ventanas
        self.lista_ventanas = tk.Listbox(self.frame, width=40, height=10)
        self.lista_ventanas.pack(side=tk.LEFT, padx=5)

        # Crear un botón para cerrar la ventana seleccionada
        self.boton_cerrar = tk.Button(self, text="Cerrar Ventana", command=self.cerrar_ventana)
        self.boton_cerrar.pack(pady=5)

        # Crear un botón para refrescar la lista de ventanas
        self.boton_refrescar = tk.Button(self, text="Refrescar", command=self.refrescar_lista)
        self.boton_refrescar.pack(pady=5)

    def agregar_ventana(self, ventana):
        """Agrega una ventana a la lista del gestor."""
        self.ventanas.append(ventana)
        self.refrescar_lista()

    def refrescar_lista(self):
        """Refresca la lista de ventanas abiertas."""
        self.lista_ventanas.delete(0, tk.END)  # Limpiar la lista
        for ventana in self.ventanas:
            self.lista_ventanas.insert(tk.END, ventana.title())  # Agregar el título de la ventana

    def cerrar_ventana(self):
        """Cierra la ventana seleccionada de la lista."""
        seleccion = self.lista_ventanas.curselection()
        if seleccion:
            indice = seleccion[0]
            ventana_a_cerrar = self.ventanas[indice]
            ventana_a_cerrar.destroy()  # Cerrar la ventana
            del self.ventanas[indice]  # Eliminar de la lista
            self.refrescar_lista()  # Refrescar la lista de ventanas
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una ventana para cerrar.")

def main():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    gestor = GestorVentanas(root)
    gestor.mainloop()

if __name__ == "__main__":
    main()
