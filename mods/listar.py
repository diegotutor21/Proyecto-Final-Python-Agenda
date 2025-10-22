import tkinter as tk
from tkinter import ttk
from db.db import listar_contactos

# Variable global para controlar si la ventana ya está abierta
listar_win = None

def listar(root):
    global listar_win

    # Si ya existe y sigue abierta, no hacer nada
    if listar_win and listar_win.winfo_exists():
        listar_win.focus_force()
        return

    listar_win = tk.Toplevel(root)
    listar_win.title("Lista de Contactos")
    listar_win.geometry("700x500")
    listar_win.configure(bg="#f9f9f9")

    # -----------------------------
    # Encabezado
    # -----------------------------
    header = tk.Frame(listar_win, bg="#4a90e2", height=50)
    header.pack(fill="x")
    tk.Label(
        header, text="📋 Contactos Guardados",
        bg="#4a90e2", fg="white", font=("Arial", 14, "bold")
    ).pack(pady=10)

    # -----------------------------
    # Tabla de contactos
    # -----------------------------
    frame_tabla = tk.Frame(listar_win, bg="#f4fefd")
    frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

    columnas = ("Nombre", "Apellido", "Celular", "Email")
    tree = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=10)

    # Encabezados
    for col in columnas:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    tree.pack(fill="both", expand=True)

    # Cargar datos
    contactos = listar_contactos()
    for c in contactos:
        tree.insert("", tk.END, values=(c["nombre"], c["apellido"], c["celular"], c["email"]))

    # -----------------------------
    # Botón volver
    # -----------------------------
    btn_frame = tk.Frame(listar_win, bg="#f9f9f9")
    btn_frame.pack(pady=10)

    tk.Button(
        btn_frame,
        text="Volver a Inicio",
        command=listar_win.destroy,
        bg="#e74c3c",
        fg="white",
        font=("Arial", 11, "bold"),
        activebackground="#c0392b",
        relief="flat",
        width=18,
        height=2
    ).pack()
