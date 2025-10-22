import tkinter as tk
from tkinter import ttk, messagebox
from db.db import listar_contactos, delete_contact

# Variable para controlar si la ventana está abierta
eliminar_win = None

def eliminar(root):
    global eliminar_win

    # Si ya existe y sigue abierta, enfocarla en vez de abrir otra
    if eliminar_win and eliminar_win.winfo_exists():
        eliminar_win.focus_force()
        return
    
    eliminar_win = tk.Toplevel(root)
    eliminar_win.title("Eliminar Contacto")
    eliminar_win.geometry("700x500")
    eliminar_win.configure(bg="#f9f9f9")

    # -----------------------------
    # Encabezado
    # -----------------------------
    header = tk.Frame(eliminar_win, bg="#4a90e2", height=50)
    header.pack(fill="x")
    tk.Label(
        header, text="❌ Eliminar Contacto",
        bg="#4a90e2", fg="white", font=("Arial", 14, "bold")
    ).pack(pady=10)

    # -----------------------------
    # Tabla de contactos
    # -----------------------------
    frame_tabla = tk.Frame(eliminar_win, bg="#f4fefd")
    frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

    columnas = ("ID", "Nombre", "Apellido", "Celular", "Email")
    columnas_visibles = ("Nombre", "Apellido", "Celular", "Email")
    tree = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=10, displaycolumns=columnas_visibles)

    for col in columnas_visibles:  # Solo configura las columnas visibles
        tree.heading(col, text=col)
        tree.column(col, width=120)
        tree.pack(fill="both", expand=True)

    # -----------------------------
    # Función para recargar datos
    # -----------------------------
    def cargar_contactos():
        for fila in tree.get_children():
            tree.delete(fila)
        contactos = listar_contactos()
        for c in contactos:
            tree.insert("", tk.END, values=(c["id"], c["nombre"], c["apellido"], c["celular"], c["email"]))

    cargar_contactos()

    # -----------------------------
    # Función para eliminar
    # -----------------------------
    def eliminar_contacto():
        seleccion = tree.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione un contacto para eliminar.")
            return

        item = tree.item(seleccion[0])
        contacto_id = item["values"][0]
        nombre = item["values"][1]
        apellido = item["values"][2]

        confirmar = messagebox.askyesno("Confirmar", f"¿Eliminar a {nombre} {apellido}?")
        if confirmar:
            if delete_contact(contacto_id):
                messagebox.showinfo("Éxito", "Contacto eliminado correctamente.")
                cargar_contactos()
                eliminar_win.destroy()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el contacto.")

    # -----------------------------
    # Botones inferiores
    # -----------------------------
    btn_frame = tk.Frame(eliminar_win, bg="#f9f9f9")
    btn_frame.pack(pady=10)

    tk.Button(
        btn_frame, text="Eliminar seleccionado", command=eliminar_contacto,
        bg="#3498db", fg="white", font=("Arial", 11, "bold"),
        activebackground="#2980b9", relief="flat", width=20, height=2
    ).grid(row=0, column=0, padx=10)

    tk.Button(
        btn_frame, text="Volver al inicio", command=eliminar_win.destroy,
        bg="#e74c3c", fg="white", font=("Arial", 11, "bold"),
        activebackground="#c0392b", relief="flat", width=20, height=2
    ).grid(row=0, column=1, padx=10)
