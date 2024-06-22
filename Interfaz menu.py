from tkinter import Tk, Label, Entry, Button, Frame, PhotoImage, font, messagebox, Canvas, Scrollbar
import os
from Autor import Autor
from Libro import Libro
from Usuario import Usuario
from Categoria import Categoria
from Biblioteca import Biblioteca

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca Socrática")

        self.bg_color = "#FDF5E6"
        self.label_color = "#8B4513"
        self.button_color = "#E3C565"
        self.button_hover_color = "#D1B46F"
        self.button_text_color = "#8B4513"
        self.entry_bg_color = "#FFF8DC"

        self.root.configure(background=self.bg_color)

        # Frame principal para la interfaz con scrollbar
        self.main_frame = Frame(root, bg=self.bg_color)
        self.main_frame.pack(fill='both', expand=True)

        self.canvas = Canvas(self.main_frame, bg=self.bg_color)
        self.canvas.pack(side='left', fill='both', expand=True)

        self.scrollbar = Scrollbar(self.main_frame, orient='vertical', command=self.canvas.yview)
        self.scrollbar.pack(side='right', fill='y')

        self.interior_frame = Frame(self.canvas, bg=self.bg_color)
        self.canvas.create_window((0, 0), window=self.interior_frame, anchor='nw')

        image_path = os.path.join("C:/Users/Lisbeth cordero/IdeaProjects/Python/Gestion de Biblioteca", 'Biblioteca.png')
        self.image = PhotoImage(file=image_path)
        self.image_label = Label(self.interior_frame, image=self.image, bg=self.bg_color)
        self.image_label.grid(row=0, columnspan=2, pady=(0, 20))

        font_style = font.Font(family="Helvetica", size=12, weight="bold")

        Label(self.interior_frame, text="Nombre completo de Usuario:", bg=self.bg_color, fg=self.label_color, font=font_style).grid(row=1, column=0, pady=5, sticky="w")
        self.usuario_entry = Entry(self.interior_frame, bg=self.entry_bg_color)
        self.usuario_entry.grid(row=1, column=1, pady=5, padx=10)

        Label(self.interior_frame, text="Número de Identificación:", bg=self.bg_color, fg=self.label_color, font=font_style).grid(row=2, column=0, pady=5, sticky="w")
        self.id_entry = Entry(self.interior_frame, bg=self.entry_bg_color)
        self.id_entry.grid(row=2, column=1, pady=5, padx=10)

        Label(self.interior_frame, text="Nombre del Libro:", bg=self.bg_color, fg=self.label_color, font=font_style).grid(row=3, column=0, pady=5, sticky="w")
        self.libro_entry = Entry(self.interior_frame, bg=self.entry_bg_color)
        self.libro_entry.grid(row=3, column=1, pady=5, padx=10)

        Label(self.interior_frame, text="Autor del Libro:", bg=self.bg_color, fg=self.label_color, font=font_style).grid(row=4, column=0, pady=5, sticky="w")
        self.autor_entry = Entry(self.interior_frame, bg=self.entry_bg_color)
        self.autor_entry.grid(row=4, column=1, pady=5, padx=10)

        Label(self.interior_frame, text="Categoría del Libro:", bg=self.bg_color, fg=self.label_color, font=font_style).grid(row=5, column=0, pady=5, sticky="w")
        self.categoria_entry = Entry(self.interior_frame, bg=self.entry_bg_color)
        self.categoria_entry.grid(row=5, column=1, pady=5, padx=10)

        self.boton_prestamo = Button(self.interior_frame, text="Realizar Préstamo", bg=self.button_color, fg=self.button_text_color, font=font_style, command=self.realizar_prestamo_ejemplo)
        self.boton_prestamo.grid(row=6, columnspan=2, pady=10)
        self.boton_prestamo.bind("<Enter>", self.on_enter)
        self.boton_prestamo.bind("<Leave>", self.on_leave)

        self.boton_mostrar_registros = Button(self.interior_frame, text="Mostrar Registros", bg=self.button_color, fg=self.button_text_color, font=font_style, command=self.mostrar_registros)
        self.boton_mostrar_registros.grid(row=7, columnspan=2, pady=10)
        self.boton_mostrar_registros.bind("<Enter>", self.on_enter)
        self.boton_mostrar_registros.bind("<Leave>", self.on_leave)

        self.registros = []

        self.biblioteca = Biblioteca()

        self.root.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.root.geometry(f"{self.interior_frame.winfo_reqwidth()}x{self.interior_frame.winfo_reqheight()}")

    def on_enter(self, e):
        e.widget['background'] = self.button_hover_color

    def on_leave(self, e):
        e.widget['background'] = self.button_color

    def realizar_prestamo_ejemplo(self):
        nombre_usuario = self.usuario_entry.get()
        id_usuario = self.id_entry.get()
        nombre_libro = self.libro_entry.get()
        autor_libro = self.autor_entry.get()
        categoria_libro = self.categoria_entry.get()

        autor = Autor(autor_libro, "")
        categoria = Categoria(categoria_libro)
        libro = Libro(nombre_libro, "", autor, categoria)
        usuario = Usuario(nombre_usuario, "", id_usuario)

        prestamo = {
            "Usuario": usuario,
            "Libro": libro
        }
        self.biblioteca.realizar_prestamo(prestamo)

        messagebox.showinfo("Préstamo realizado", "El préstamo se realizó con éxito.")

        self.usuario_entry.delete(0, 'end')
        self.id_entry.delete(0, 'end')
        self.libro_entry.delete(0, 'end')
        self.autor_entry.delete(0, 'end')
        self.categoria_entry.delete(0, 'end')

    def mostrar_registros(self):
        registros_texto = ""
        for prestamo in self.biblioteca.get_prestamos():
            usuario = prestamo["Usuario"]
            libro = prestamo["Libro"]

            registros_texto += f"Nombre de Usuario: {usuario.get_nombre()} {usuario.get_apellido()}\n"
            registros_texto += f"Número de Identificación: {usuario.get_id_usuario()}\n"
            registros_texto += f"Título del Libro: {libro.get_titulo()}\n"
            registros_texto += f"Autor del Libro: {libro.get_autor().get_nombre()} {libro.get_autor().get_apellido()}\n"
            registros_texto += f"Categoría del Libro: {libro.get_categoria().get_nombre()}\n"
            registros_texto += "-" * 40 + "\n"

        messagebox.showinfo("Registros de Préstamos", registros_texto)


if __name__ == "__main__":
    root = Tk()
    menu = Menu(root)
    root.mainloop()
