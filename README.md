# Proyecto-Final-Python-Agenda
Aplicación de Agenda de Contactos en Python con Tkinter y SQLite (Proyecto Final del curso de Python).
# 📒 Agenda de Contactos en Python

Aplicación de Agenda de Contactos desarrollada con **Python**, **Tkinter** y **SQLite**.  
Proyecto final aprobado del *Curso Introductorio de Python*.

---

## 🚀 Funcionalidades

- ✅ Agregar nuevos contactos  
- ✅ Listar contactos guardados  
- ✅ Modificar contactos existentes  
- ✅ Eliminar contactos  
- ✅ Validaciones (nombre, apellido, celular, email)  
- ✅ Persistencia de datos en base SQLite (`contactos.db`)

---

## 🖼️ Interfaz
La aplicación cuenta con una interfaz moderna y sencilla creada con **Tkinter**, organizada por módulos (`mods/`) para mantener el código limpio y reutilizable.

---

## 🧱 Estructura del Proyecto
```plaintext
Proyecto-Final-Python-Agenda/
├── gui.py              # Archivo principal (interfaz)
├── db/                 # Conexión y operaciones de base de datos
│   ├── db.py
│   └── contactos.db
├── mods/               # Módulos de ventanas
│   ├── alta.py
│   ├── listar.py
│   ├── modificar.py
│   └── eliminar.py
├── README.md           # Documentación del proyecto
└── Agenda.exe          # Ejecutable (no se incluye en GitHub)
```
---

## ▶️ Ejecución
### Opción A – Desde Python:
```
python gui.py
```

### Opción B – Crear ejecutable (.exe):

1. Instalar el paquete `auto-py-to-exe`
```
pip install auto-py-to-exe
```

2. Ejecutar:
```
auto-py-to-exe
```

3. En la ventana del programa:

    - En **Script location**, seleccionar `gui.py`

    - En **Settings → Output Directory**, elegir la carpeta raíz del proyecto (donde están `gui.py, db/, mods/`)

    - En **Advanced → Name**, escribir: `Agenda de Contactos`

    - En **Conversion Options**, marcar:

        - ✅ One File

        - ✅ Window Based (Sin consola)

    - En **Additional Files**, agregar:

        - Carpeta `db/`

        - Carpeta `mods/`

4. Presionar **Convert .py to .exe**

El archivo `.exe` se generará dentro de la carpeta seleccionada.

---

## 📊 Datos de Prueba
El proyecto incluye una base de datos (contactos.db) con contactos de ejemplo para probar las funciones de modificación y eliminación.

---

## 🧑‍💻 Autor
Diego Tutor
Proyecto final aprobado – Curso Introductorio de Python (2025)
📫 benjatutor12@gmail.com