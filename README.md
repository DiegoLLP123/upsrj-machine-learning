# Gestor de Textos Frecuentes
**Autor:** Diego Leonardo Larios Peralta
Este proyecto permite crear, editar, visualizar, exportar e importar configuraciones de **textos frecuentes**. Cada configuración puede contener hasta 10 textos diferentes, los cuales se pueden copiar al portapapeles fácilmente. Cuenta con **interfaz de terminal** y **GUI**.

---

## Características

- Crear nuevas configuraciones con hasta 10 textos.
- Editar textos existentes.
- Visualizar y copiar textos al portapapeles.
- Eliminar configuraciones completas.
- Exportar configuraciones a **Excel** o **CSV**.
- Importar configuraciones desde archivos **CSV**.
- Interfaz terminal interactiva con selección de opciones mediante flechas.
- Interfaz gráfica (GUI) intuitiva en Tkinter.

---

## Instalación

1. Clona este repositorio o descarga los archivos `main.py` y `config_utils.py`.
2. Instala las dependencias:

```bash
pip install pandas pyperclip pick openpyxl
```

> **Nota:** `threading` y `tkinter` son módulos estándar de Python, no requieren instalación adicional.

---

## Uso

### Terminal

Ejecuta:

```bash
python main.py
```

- Aparecerá un menú en la terminal con opciones numeradas.
- Navega con números o flechas según la función:
  - Crear configuración
  - Editar texto
  - Ver configuración y copiar textos
  - Exportar a Excel/CSV
  - Importar desde CSV
  - Abrir GUI
  - Salir

### GUI

- Al iniciar el programa, puedes abrir la GUI desde el menú terminal o ejecutando directamente `main_gui()`.
- Funcionalidades:
  - Crear configuración
  - Editar textos en ventana con campos individuales
  - Ver configuración y copiar textos con un clic
  - Exportar seleccionando directamente Excel o CSV (sin escribir la palabra)
  - Importar CSV
  - Eliminar configuraciones

---

## Estructura de Archivos

- `main.py` → archivo principal con terminal y GUI.
- `config_utils.py` → funciones para manejar configuraciones, importar/exportar y operaciones básicas.
- `configuraciones.csv` → archivo generado automáticamente que almacena todas las configuraciones.

---

## Ejemplo de Uso

1. Ejecuta `main.py`.
2. Crea una configuración llamada `Trabajo`.
3. Edita los textos 0-9 según tus necesidades.
4. Visualiza la configuración y copia cualquier texto al portapapeles.
5. Exporta la configuración a Excel o CSV para respaldo.
6. Importa configuraciones de otro archivo CSV.

---

## Dependencias

- [pandas](https://pandas.pydata.org/)
- [pyperclip](https://pypi.org/project/pyperclip/)
- [pick](https://pypi.org/project/pick/)
- [openpyxl](https://pypi.org/project/openpyxl/)

---

## Licencia

Este proyecto es **open-source** y puedes modificarlo según tus necesidades.
