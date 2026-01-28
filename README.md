Organizador de Archivos en la Carpeta Descargas
==============================================

Autor:
Diego Leonardo Larios Peralta

Descripción:
Este script en Python organiza automáticamente los archivos de la carpeta Descargas en subcarpetas según su tipo. Utiliza pandas y numpy para manejar la información de los archivos y shutil para moverlos a sus respectivas carpetas.

Las categorías de archivos que organiza incluyen: PDFs, imágenes, videos, música, documentos, programas y archivos comprimidos.

Requisitos:
- Python 3.6 o superior
- Librerías de Python:
  - pandas
  - numpy
  - os y shutil (incluidas en la librería estándar)

Puedes instalar las librerías necesarias usando:

pip install pandas numpy

Uso:
1. Coloca el archivo Automatización.py en cualquier ubicación.
2. Abre la terminal o CMD y navega hasta la carpeta donde está el script:
cd ruta/del/archivo

3. Ejecuta el script:
python Automatización.py

4. El script:
   - Detecta la carpeta Descargas del usuario.
   - Escanea todos los archivos presentes.
   - Crea subcarpetas según el tipo de archivo (si no existen).
   - Mueve cada archivo a la carpeta correspondiente.

5. Al finalizar, mostrará el mensaje:
✅ Organización completada usando pandas y numpy

Estructura de Carpetas que Crea:

Carpeta        | Extensiones Asociadas
---------------|----------------------
PDFs           | .pdf
Imagenes       | .jpg, .jpeg, .png, .gif
Videos         | .mp4, .avi, .mkv
Musica         | .mp3, .wav
Documentos     | .docx, .txt, .xlsx, .pptx
Programas      | .exe, .msi
Comprimidos    | .zip, .rar

Funcionalidad Adicional:
- Detecta automáticamente la ubicación de la carpeta Descargas en sistemas Linux mediante el archivo ~/.config/user-dirs.dirs.
- Si no se encuentra, utiliza la ruta por defecto ~/Downloads.
- Evita errores si no hay archivos para organizar.

Licencia:
Este proyecto es de uso personal y educativo. Puedes modificarlo según tus necesidades.

Notas:
- Se recomienda cerrar programas que puedan estar usando archivos en Descargas antes de ejecutar el script para evitar errores al moverlos.
- El script sobrescribirá archivos con el mismo nombre en las carpetas destino si ya existen.
