import tkinter as tk
from tkinter import ttk, messagebox
from db.db import listar_contactos, get_contact_by_id, update_contact

# Variable para controlar si la ventana está abierta
modificar_win = None

def modificar(root):
    global modificar_win

    # Si ya existe y sigue abierta, enfocarla en vez de abrir otra
    if modificar_win and modificar_win.winfo_exists():
        modificar_win.focus_force()
        return
    
    modificar_win = tk.Toplevel(root)
    modificar_win.title("Modificar Contacto")
    modificar_win.geometry("700x500")
    modificar_win.configure(bg="#f9f9f9")

    # -----------------------------
    # Encabezado
    # -----------------------------
    header = tk.Frame(modificar_win, bg="#4a90e2", height=50)
    header.pack(fill="x")
    tk.Label(
        header, text="✏️ Modificar Contacto",
        bg="#4a90e2", fg="white", font=("Arial", 14, "bold")
    ).pack(pady=10)

    # -----------------------------
    # Tabla de contactos
    # -----------------------------
    frame_tabla = tk.Frame(modificar_win, bg="#f4fefd")
    frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

    columnas = ("ID", "Nombre", "Apellido", "Celular", "Email")
    columnas_visibles = ("Nombre", "Apellido", "Celular", "Email") # Solo las columnas visibles
    tree = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=10, displaycolumns=columnas_visibles)

    for col in columnas_visibles:  # Solo configura las columnas visibles
        tree.heading(col, text=col)
        tree.column(col, width=120)

    tree.pack(fill="both", expand=True)

    # -----------------------------
    # Cargar contactos en la tabla
    # -----------------------------
    def cargar_contactos():
        for fila in tree.get_children():
            tree.delete(fila)
        contactos = listar_contactos()
        for c in contactos:
            tree.insert("", tk.END, values=(c["id"], c["nombre"], c["apellido"], c["celular"], c["email"]))

    cargar_contactos()

    # -----------------------------
    # Editar contacto
    # -----------------------------
    def editar_contacto():
        seleccion = tree.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione un contacto para modificar.")
            return

        item = tree.item(seleccion[0])
        contacto_id = item["values"][0]
        contacto = get_contact_by_id(contacto_id)

        if not contacto:
            messagebox.showerror("Error", "No se pudo cargar el contacto.")
            return

        edit_win = tk.Toplevel(modificar_win)
        edit_win.title("Editar Contacto")
        edit_win.geometry("400x300")
        edit_win.configure(bg="#f9f9f9")

        # Encabezado en editar
        header_edit = tk.Frame(edit_win, bg="#4a90e2", height=40)
        header_edit.pack(fill="x")
        tk.Label(
            header_edit, text="Editar Datos",
            bg="#4a90e2", fg="white", font=("Arial", 13, "bold")
        ).pack(pady=8)

        # Formulario
        form = tk.Frame(edit_win, bg="#f9f9f9")
        form.pack(pady=15)

        tk.Label(form, text="Nombre:", bg="#f9f9f9").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        entry_nombre = tk.Entry(form)
        entry_nombre.insert(0, contacto["nombre"])
        entry_nombre.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form, text="Apellido:", bg="#f9f9f9").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        entry_apellido = tk.Entry(form)
        entry_apellido.insert(0, contacto["apellido"])
        entry_apellido.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form, text="Celular:", bg="#f9f9f9").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        entry_celular = tk.Entry(form)
        entry_celular.insert(0, contacto["celular"])
        entry_celular.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(form, text="Email:", bg="#f9f9f9").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        entry_email = tk.Entry(form)
        entry_email.insert(0, contacto["email"] if contacto["email"] else "")
        entry_email.grid(row=3, column=1, padx=10, pady=5)

        # Guardar cambios
        def guardar_cambios():
            nuevo_nombre = entry_nombre.get().strip()
            nuevo_apellido = entry_apellido.get().strip()
            nuevo_celular = entry_celular.get().strip()
            nuevo_email = entry_email.get().strip()

            # Validaciones
            if nuevo_nombre and not nuevo_nombre.isalpha():
                messagebox.showerror("Error", "El nombre debe contener solo letras.")
                return
            if nuevo_apellido and not nuevo_apellido.isalpha():
                messagebox.showerror("Error", "El apellido debe contener solo letras.")
                return
            if nuevo_celular and not nuevo_celular.isdigit():
                messagebox.showerror("Error", "El celular debe contener solo números.")
                return
            if nuevo_email and not ("@" in nuevo_email and "." in nuevo_email):
                messagebox.showerror("Error", "Email inválido.")
                return

            ok = update_contact(
                contacto_id,
                nombre=nuevo_nombre,
                apellido=nuevo_apellido,
                celular=nuevo_celular,
                email=nuevo_email
            )

            if ok:
                messagebox.showinfo("Éxito", "Contacto modificado correctamente.")
                edit_win.destroy()
                modificar_win.destroy()

                cargar_contactos()
            else:
                messagebox.showwarning("Aviso", "No se realizaron cambios.")

        tk.Button(
            edit_win, text="💾 Guardar cambios", command=guardar_cambios,
            bg="#2ecc71", fg="white", font=("Arial", 11, "bold"),
            activebackground="#27ae60", relief="flat", width=18, height=1
        ).pack(pady=15)

    # -----------------------------
    # Botones inferiores
    # -----------------------------
    btn_frame = tk.Frame(modificar_win, bg="#f9f9f9")
    btn_frame.pack(pady=10)

    tk.Button(
        btn_frame, text="Editar seleccionado", command=editar_contacto,
        bg="#3498db", fg="white", font=("Arial", 11, "bold"),
        activebackground="#2980b9", relief="flat", width=20, height=2
    ).grid(row=0, column=0, padx=10)

    tk.Button(
        btn_frame, text="Volver al inicio", command=modificar_win.destroy,
        bg="#e74c3c", fg="white", font=("Arial", 11, "bold"),
        activebackground="#c0392b", relief="flat", width=20, height=2
    ).grid(row=0, column=1, padx=10)

