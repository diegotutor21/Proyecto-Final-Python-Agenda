import sqlite3
from sqlite3 import IntegrityError
# Configuración de la base de datos
import os
DB_NAME = os.path.join(os.path.dirname(__file__), "contactos.db")

# ----------------------------------------
# Función de conexión
# ----------------------------------------
def conectar():
    """
    Abre una conexión a la base de datos y devuelve el objeto conexión.
    """
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Para acceder a las columnas por nombre
    return conn

# ----------------------------------------
# Crear tabla (si no existe)
# ----------------------------------------
def crear_tabla():
    """
    Crea la tabla 'contactos' en la base de datos si aún no existe.
    """
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS contactos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                celular TEXT NOT NULL UNIQUE,
                email TEXT
            )
        """)
        conn.commit()

# ----------------------------------------
# Insertar un contacto
# ----------------------------------------
def insertar_contacto(nombre, apellido, celular, email=None):
    """
    Inserta un nuevo contacto en la tabla.
    Devuelve el ID asignado automáticamente.
    """
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO contactos (nombre, apellido, celular, email) VALUES (?, ?, ?, ?)",
            (nombre, apellido, celular, email)
        )
        conn.commit()
        return cur.lastrowid

# ----------------------------------------
# Listar todos los contactos
# ----------------------------------------
def listar_contactos():
    """
    Devuelve una lista con todos los contactos de la tabla.
    """
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM contactos ORDER BY id")
        filas = cur.fetchall()
        return [dict(fila) for fila in filas]

# ----------------------------------------
# Buscar un contacto por ID
# ----------------------------------------
def get_contact_by_id(contacto_id):  # 🔹 renombrado
    """
    Busca un contacto por su ID. Devuelve un diccionario o None.
    """
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM contactos WHERE id = ?", (contacto_id,))
        fila = cur.fetchone()
        return dict(fila) if fila else None

# ----------------------------------------
# Actualizar un contacto
# ----------------------------------------
def update_contact(contacto_id, nombre=None, apellido=None, celular=None, email=None):  # 🔹 renombrado
    """
    Actualiza un contacto existente.
    Solo cambia los campos que reciban un valor distinto de None.
    """
    campos = []
    valores = []

    if nombre is not None:
        campos.append("nombre = ?")
        valores.append(nombre)
    if apellido is not None:
        campos.append("apellido = ?")
        valores.append(apellido)
    if celular is not None:
        campos.append("celular = ?")
        valores.append(celular)
    if email is not None:
        campos.append("email = ?")
        valores.append(email)

    if not campos:
        return False  # No hay nada para actualizar

    valores.append(contacto_id)
    consulta = f"UPDATE contactos SET {', '.join(campos)} WHERE id = ?"

    with conectar() as conn:
        cur = conn.cursor()
        cur.execute(consulta, valores)
        conn.commit()
        return cur.rowcount > 0  # True si se modificó algo

# ----------------------------------------
# Eliminar un contacto
# ----------------------------------------
def delete_contact(contacto_id):  # 🔹 renombrado
    """
    Elimina un contacto por su ID.
    """
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM contactos WHERE id = ?", (contacto_id,))
        conn.commit()
        return cur.rowcount > 0

# ----------------------------------------
# Ejecutar directamente este archivo
# ----------------------------------------
if __name__ == "__main__":
    crear_tabla()
    print("Base de datos inicializada:", DB_NAME)
