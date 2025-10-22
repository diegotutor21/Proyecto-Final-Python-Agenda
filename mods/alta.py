import tkinter as tk
from tkinter import messagebox
from db.db import insertar_contacto
from sqlite3 import IntegrityError

# Variable para controlar si la ventana está abierta
agregar_win = None

def agregar(root):
    global agregar_win

    # Si ya existe y sigue abierta, enfocarla en vez de abrir otra
    if agregar_win and agregar_win.winfo_exists():
        agregar_win.focus_force()
        return
    
    agregar_win = tk.Toplevel(root)
    agregar_win.title("Agregar Contacto")
    agregar_win.geometry("400x320")
    agregar_win.configure(bg="#f9f9f9")

    # -----------------------------
    # Encabezado
    # -----------------------------
    header = tk.Frame(agregar_win, bg="#4a90e2", height=50)
    header.pack(fill="x")
    tk.Label(
        header, text="➕ Nuevo Contacto",
        bg="#4a90e2", fg="white", font=("Arial", 14, "bold")
    ).pack(pady=10)

    # -----------------------------
    # Contenedor del formulario
    # -----------------------------
    form = tk.Frame(agregar_win, bg="#f9f9f9")
    form.pack(pady=20)

    tk.Label(form, text="Nombre:", bg="#f9f9f9", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=8, sticky="e")
    entry_nombre = tk.Entry(form, font=("Arial", 11))
    entry_nombre.grid(row=0, column=1, padx=10, pady=8)

    tk.Label(form, text="Apellido:", bg="#f9f9f9", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=8, sticky="e")
    entry_apellido = tk.Entry(form, font=("Arial", 11))
    entry_apellido.grid(row=1, column=1, padx=10, pady=8)

    tk.Label(form, text="Celular:", bg="#f9f9f9", font=("Arial", 11)).grid(row=2, column=0, padx=10, pady=8, sticky="e")
    entry_celular = tk.Entry(form, font=("Arial", 11))
    entry_celular.grid(row=2, column=1, padx=10, pady=8)

    tk.Label(form, text="Email:", bg="#f9f9f9", font=("Arial", 11)).grid(row=3, column=0, padx=10, pady=8, sticky="e")
    entry_email = tk.Entry(form, font=("Arial", 11))
    entry_email.grid(row=3, column=1, padx=10, pady=8)

    # -----------------------------
    # Guardar contacto
    # -----------------------------
    def guardar():
        nombre = entry_nombre.get().strip()
        apellido = entry_apellido.get().strip()
        celular = entry_celular.get().strip()
        email = entry_email.get().strip()

        if not nombre.isalpha():
            messagebox.showerror("Error", "El nombre debe contener solo letras.")
            return
        if not apellido.isalpha():
            messagebox.showerror("Error", "El apellido debe contener solo letras.")
            return
        if not celular.isdigit():
            messagebox.showerror("Error", "El celular debe contener solo números.")
            return
        if not ("@" in email and "." in email):
            messagebox.showerror("Error", "El email debe ser válido.")
            return

        try:
            insertar_contacto(nombre, apellido, celular, email)
            messagebox.showinfo("Éxito", "Contacto guardado correctamente.")
            agregar_win.destroy()
        except IntegrityError:
            messagebox.showerror("Error", "Ya existe un contacto con ese celular.")

    # -----------------------------
    # Botones inferiores
    # -----------------------------
    botones = tk.Frame(agregar_win, bg="#f9f9f9")
    botones.pack(pady=10)

    tk.Button(botones, text="Guardar", command=guardar,
              bg="#2ecc71", fg="white", font=("Arial", 11, "bold"),
              activebackground="#27ae60", relief="flat", width=12).grid(row=0, column=0, padx=10)

    tk.Button(botones, text="Volver", command=agregar_win.destroy,
              bg="#e74c3c", fg="white", font=("Arial", 11, "bold"),
              activebackground="#c0392b", relief="flat", width=12).grid(row=0, column=1, padx=10)
