import tkinter as tk
from tkinter import ttk
from mods.alta import agregar
from mods.listar import listar
from mods.modificar import modificar
from mods.eliminar import eliminar
from db.db import crear_tabla

def main():
    crear_tabla() 

    root = tk.Tk()
    root.title("Agenda de Contactos")
    root.geometry("380x560")
    root.configure(bg="#f8fafc")
    root.resizable(False, False)

    # Aplicar estilo ttk
    style = ttk.Style()
    style.theme_use('clam')

    # -----------------------------
    # Encabezado con Canvas (simulando gradiente)
    # -----------------------------
    header = tk.Canvas(root, height=80, width=400, bg="#2563eb", highlightthickness=0)
    header.pack(fill="x")
    header.create_rectangle(0, 0, 400, 80, fill="#2563eb", outline="")
    header.create_text(190, 28, text="📱 AGENDA DE CONTACTOS", fill="white", font=("Segoe UI", 16, "bold"))
    header.create_text(190, 55, text="Gestiona tus contactos fácilmente", fill="#bfdbfe", font=("Segoe UI", 9))

    # -----------------------------
    # Contenedor principal
    # -----------------------------
    main_container = tk.Frame(root, bg="#f8fafc")
    main_container.pack(expand=True, fill="both", pady=30)

    # Estilo base para botones
    def crear_boton(parent, texto, icono, comando, color="#3b82f6"):
        btn = tk.Button(
            parent,
            text=f"{icono}  {texto}",
            command=comando,
            font=("Segoe UI", 11, "normal"),
            bg=color,
            fg="white",
            activebackground="#1d4ed8" if color == "#3b82f6" else "#dc2626",
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=20,
            pady=12
        )
        btn.pack(pady=10, fill="x", padx=40)

        # Efectos hover
        def on_enter(e):
            btn.configure(bg="#1d4ed8" if color == "#3b82f6" else "#dc2626")
        def on_leave(e):
            btn.configure(bg=color)

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

        return btn

    # Botones principales
    crear_boton(main_container, "Agregar Contacto", "➕", lambda: agregar(root))
    crear_boton(main_container, "Ver Contactos", "📋", lambda: listar(root))
    crear_boton(main_container, "Modificar", "✏️", lambda: modificar(root))
    crear_boton(main_container, "Eliminar", "❌", lambda: eliminar(root))

    # Botón salir más destacado
    crear_boton(main_container, "Salir", "🚪", root.quit, color="#ef4444")

    # -----------------------------
    # Footer sutil
    # -----------------------------
    footer = tk.Frame(root, bg="#e2e8f0", height=30)
    footer.pack(fill="x", side="bottom")

    tk.Label(
        footer,
        text="© 2024 - Tu Agenda Personal",
        bg="#e2e8f0",
        fg="#475569",
        font=("Segoe UI", 8)
    ).pack(pady=6)

    # Centrar la ventana
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")

    root.mainloop()

if __name__ == "__main__":
    main()
