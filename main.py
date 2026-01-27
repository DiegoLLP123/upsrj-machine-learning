import config_utils as cu
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import pyperclip
import threading

# Para selección con flechas
from pick import pick

# === Estado compartido ===
gui_abierta = False
terminar_programa = False

# === Terminal ===
def menu_terminal():
    global gui_abierta, terminar_programa
    while not terminar_programa:
        print("\n=== Gestor Textos Frecuentes (Terminal) ===")
        print("1. Crear configuración")
        print("2. Editar texto")
        print("3. Ver configuración")
        print("4. Exportar")
        print("5. Importar CSV")
        if gui_abierta:
            print("6. Abrir GUI (ya está abierta)")
        else:
            print("6. Abrir GUI")
        print("0. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            crear_config_terminal()
        elif opcion == "2":
            editar_terminal()
        elif opcion == "3":
            ver_terminal()
        elif opcion == "4":
            exportar_terminal()
        elif opcion == "5":
            importar_terminal()
        elif opcion == "6":
            if not gui_abierta:
                threading.Thread(target=main_gui, daemon=True).start()
            else:
                print("La GUI ya está abierta.")
        elif opcion == "0":
            terminar_programa = True
            break
        else:
            print("Opción inválida.")

# --- Funciones Terminal ---
def crear_config_terminal():
    config = input("Nombre de nueva configuración: ").strip()
    if not config:
        print("Nombre inválido."); return
    if config in cu.listar_configuraciones():
        print("Ya existe esa configuración."); return
    for i in range(10):
        cu.agregar_texto(config, i, "")
    print(f"Configuración '{config}' creada con 10 textos vacíos.")

def seleccionar_config_terminal():
    configs = cu.listar_configuraciones()
    if not configs:
        print("No hay configuraciones. Crea una antes.")
        return None
    opcion, indice = pick(configs, "Selecciona configuración con flechas y Enter:")
    return opcion

def editar_terminal():
    config = seleccionar_config_terminal()
    if not config: return
    textos = cu.listar_textos(config)
    for i, t in enumerate(textos):
        print(f"{i}: {t[:40]}" if t else f"{i}: [Vacío]")
    numero = input("Número 0-9 a editar: ").strip()
    if numero not in [str(i) for i in range(10)]:
        print("Número inválido"); return
    texto = input("Nuevo texto: ")
    cu.editar_texto(config, numero, texto)
    print("Editado correctamente.")

def ver_terminal():
    config = seleccionar_config_terminal()
    if not config: return
    textos = cu.listar_textos(config)
    print(f"\n=== {config} ===")
    for i, t in enumerate(textos):
        print(f"{i}: {t[:40]}" if t else f"{i}: [Vacío]")

    print("\nSi deseas copiar un texto, ingresa su número 0-9.")
    print("Si deseas eliminar la configuración, ingresa 00.")

    opcion = input("Número (Enter para salir): ").strip()
    if opcion in [str(i) for i in range(10)]:
        if cu.copiar_texto(config, opcion):
            print("Texto copiado al portapapeles.")
        else:
            print("No hay texto asignado en ese número.")
    elif opcion == "00":
        confirmar = input(f"¿Deseas eliminar la configuración '{config}'? (s/n): ").strip().lower()
        if confirmar == "s":
            for i in range(10):
                cu.eliminar_texto(config, i)
            print(f"Configuración '{config}' eliminada correctamente.")
        else:
            print("No se eliminó la configuración.")

def exportar_terminal():
    import tkinter as tk
    root = tk.Tk()
    root.withdraw()

    tipo = input("Exportar como (1) Excel o (2) CSV? ").strip()
    if tipo == "1":
        ruta = asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel","*.xlsx")])
        if ruta:
            try:
                cu.exportar_excel(ruta)
                print("Exportado a Excel correctamente.")
            except ModuleNotFoundError:
                print("Error: necesitas instalar openpyxl para exportar Excel (pip install openpyxl).")
    elif tipo == "2":
        ruta = asksaveasfilename(defaultextension=".csv", filetypes=[("CSV","*.csv")])
        if ruta:
            cu.exportar_csv(ruta)
            print("Exportado a CSV correctamente.")
    else:
        print("Opción inválida.")

    root.destroy()

def importar_terminal():
    import tkinter as tk
    root = tk.Tk()
    root.withdraw()
    ruta = askopenfilename(filetypes=[("CSV","*.csv")])
    if ruta:
        if cu.importar_csv(ruta):
            print("Importado correctamente.")
        else:
            print("CSV inválido o formato incorrecto.")
    root.destroy()

# === GUI ===
def main_gui():
    global gui_abierta
    if gui_abierta: return
    gui_abierta = True

    root = tk.Tk()
    root.title("Gestor Textos Frecuentes")
    root.geometry("600x500")

    # --- Listbox de configuraciones ---
    listbox = tk.Listbox(root)
    listbox.pack(fill=tk.BOTH, expand=True)

    # --- Funciones GUI ---
    def actualizar_listbox():
        listbox.delete(0, tk.END)
        for c in cu.listar_configuraciones():
            listbox.insert(tk.END, c)

    def crear_config_gui():
        top = tk.Toplevel(root)
        top.title("Crear configuración")
        tk.Label(top, text="Nombre configuración:").pack()
        entry = tk.Entry(top); entry.pack()
        def guardar():
            nombre = entry.get().strip()
            if not nombre: return
            if nombre in cu.listar_configuraciones(): return
            for i in range(10): cu.agregar_texto(nombre, i, "")
            actualizar_listbox()
            top.destroy()
        tk.Button(top, text="Crear", command=guardar).pack()

    def editar_gui():
        if not listbox.curselection(): return
        config = listbox.get(listbox.curselection()[0])
        top = tk.Toplevel(root)
        top.title("Editar textos")
        entries = []
        for i, t in enumerate(cu.listar_textos(config)):
            tk.Label(top, text=f"{i}:").pack()
            e = tk.Entry(top, width=50); e.insert(0, t); e.pack()
            entries.append((i, e))
        def guardar():
            for i, e in entries:
                cu.editar_texto(config, i, e.get())
            top.destroy()
        tk.Button(top, text="Guardar", command=guardar).pack()

    def ver_gui():
        if not listbox.curselection(): return
        config = listbox.get(listbox.curselection()[0])
        top = tk.Toplevel(root)
        top.title(f"Ver {config}")

        # Mostrar textos en botones para copiar
        for i, t in enumerate(cu.listar_textos(config)):
            txt = t if t else "[Vacío]"
            tk.Button(top, text=f"{i}: {txt[:40]}", width=50,
                      command=lambda t=t: pyperclip.copy(t) if t else None).pack(pady=2)

        # Botón de eliminar configuracion
        def eliminar_config():
            from tkinter import messagebox
            if messagebox.askyesno("Confirmar", f"¿Deseas eliminar la configuración '{config}'?"):
                for i in range(10):
                    cu.eliminar_texto(config, i)
                actualizar_listbox()
                top.destroy()
                messagebox.showinfo("Eliminado", f"Configuración '{config}' eliminada correctamente.")

        tk.Button(top, text="Eliminar configuración", fg="red", command=eliminar_config).pack(pady=5)

    # --- Exportar GUI actualizado ---
    def exportar_gui():
        from tkinter import messagebox

        ruta = asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel (*.xlsx)", "*.xlsx"), ("CSV (*.csv)", "*.csv")]
        )
        if not ruta:
            return  # Cancelado

        if ruta.endswith(".xlsx"):
            try:
                cu.exportar_excel(ruta)
                messagebox.showinfo("Éxito", "Exportado a Excel correctamente.")
            except ModuleNotFoundError:
                messagebox.showerror("Error", "Necesitas instalar openpyxl para exportar Excel.")
        elif ruta.endswith(".csv"):
            cu.exportar_csv(ruta)
            messagebox.showinfo("Éxito", "Exportado a CSV correctamente.")
        else:
            messagebox.showwarning("Cancelado", "Tipo de archivo no soportado.")

    def importar_gui():
        ruta = askopenfilename(filetypes=[("CSV","*.csv")])
        if ruta:
            cu.importar_csv(ruta)
            actualizar_listbox()

    def cerrar_gui():
        global gui_abierta
        gui_abierta = False
        root.destroy()

    # --- Botones GUI ---
    tk.Button(root, text="Crear configuración", command=crear_config_gui).pack()
    tk.Button(root, text="Editar texto", command=editar_gui).pack()
    tk.Button(root, text="Ver configuración", command=ver_gui).pack()
    tk.Button(root, text="Exportar", command=exportar_gui).pack()
    tk.Button(root, text="Importar CSV", command=importar_gui).pack()
    tk.Button(root, text="Salir", command=cerrar_gui).pack()

    actualizar_listbox()
    root.mainloop()
    gui_abierta = False

# === Main ===
if __name__ == "__main__":
    cu.inicializar_csv()

    # Iniciar terminal en hilo
    threading.Thread(target=menu_terminal, daemon=True).start()
    
    # Iniciar GUI en hilo
    threading.Thread(target=main_gui, daemon=True).start()
    
    # Mantener el hilo principal vivo mientras el programa no termine
    try:
        while not terminar_programa:
            threading.Event().wait(0.5)
    except KeyboardInterrupt:
        terminar_programa = True
