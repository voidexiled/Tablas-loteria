import random
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
import json


class CustomLabel(tk.Label):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image_path = ""
        self.is_bn = False


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


# Set de datos que contiene todos lo nombres de las figuras de la loteria mexicana
# y sus respectivas imagenes
data = {
    "El gallo": "assets/images/1.jpg",
    "El diablito": "assets/images/2.jpg",
    "La dama": "assets/images/3.jpg",
    "El catrin": "assets/images/4.jpg",
    "El paraguas": "assets/images/5.jpg",
    "La sirena": "assets/images/6.jpg",
    "La escalera": "assets/images/7.jpg",
    "La botella": "assets/images/8.jpg",
    "El barril": "assets/images/9.jpg",
    "El arbol": "assets/images/10.jpg",
    "El melon": "assets/images/11.jpg",
    "El valiente": "assets/images/12.jpg",
    "El gorrito": "assets/images/13.jpg",
    "La muerte": "assets/images/14.jpg",
    "La pera": "assets/images/15.jpg",
    "La bandera": "assets/images/16.jpg",
    "El bandolon": "assets/images/17.jpg",
    "El violoncello": "assets/images/18.jpg",
    "La garza": "assets/images/19.jpg",
    "El pajaro": "assets/images/20.jpg",
    "La mano": "assets/images/21.jpg",
    "La bota": "assets/images/22.jpg",
    "La luna": "assets/images/23.jpg",
    "El cotorro": "assets/images/24.jpg",
    "El borracho": "assets/images/25.jpg",
    "El negrito": "assets/images/26.jpg",
    "El corazon": "assets/images/27.jpg",
    "La sandia": "assets/images/28.jpg",
    "El tambor": "assets/images/29.jpg",
    "El camarón": "assets/images/30.jpg",
    "Las jaras": "assets/images/31.jpg",
    "El músico": "assets/images/32.jpg",
    "La araña": "assets/images/33.jpg",
    "El soldado": "assets/images/34.jpg",
    "La estrella": "assets/images/35.jpg",
    "El cazo": "assets/images/36.jpg",
    "El mundo": "assets/images/37.jpg",
    "El apache": "assets/images/38.jpg",
    "El nopal": "assets/images/39.jpg",
    "El alacrán": "assets/images/40.jpg",
    "La rosa": "assets/images/41.jpg",
    "La calavera": "assets/images/42.jpg",
    "La campana": "assets/images/43.jpg",
    "El cantarito": "assets/images/44.jpg",
    "El venado": "assets/images/45.jpg",
    "El sol": "assets/images/46.jpg",
    "La corona": "assets/images/47.jpg",
    "La chalupa": "assets/images/48.jpg",
    "El pino": "assets/images/49.jpg",
    "El pescado": "assets/images/50.jpg",
    "La palma": "assets/images/51.jpg",
    "La maceta": "assets/images/52.jpg",
    "El arpa": "assets/images/53.jpg",
    "La rana": "assets/images/54.jpg",
}


def apply_filter(image, is_bn):
    if is_bn:
        return image.convert("L")
    return image


def on_image_click(event):
    label = event.widget
    image_path = label.image_path
    is_bn = not label.is_bn

    image = Image.open(image_path)
    filtered_image = apply_filter(image, is_bn)
    filtered_image = filtered_image.resize((100, 140), Image.LANCZOS)

    filtered_image_tk = ImageTk.PhotoImage(filtered_image)
    label.configure(image=filtered_image_tk)
    label.image = filtered_image_tk
    label.is_bn = is_bn


def mostrar_tabla(tabla):
    root = tk.Tk()
    root.title("Tabla de Lotería")

    num_filas = len(tabla)
    num_columnas = len(tabla[0])
    ventana_ancho = num_columnas * 100
    ventana_alto = num_filas * 140
    root.geometry(f"{ventana_ancho+(num_columnas*5)}x{ventana_alto+(num_filas*5)}")

    for i in range(num_filas):
        for j in range(num_columnas):
            figura = tabla[i][j]
            ruta_imagen = data[figura]
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((100, 140), Image.LANCZOS)

            label = CustomLabel(root)
            label.grid(row=i, column=j)

            label.image_path = ruta_imagen

            imagen_tk = ImageTk.PhotoImage(imagen)
            label.configure(image=imagen_tk)
            label.image = imagen_tk

            label.bind("<Button-1>", on_image_click)
    center_window(root)
    root.mainloop()


def generar_matriz_aleatoria(n, m):
    if n * m <= 0:
        return []

    matrices_guardadas = cargar_matrices_guardadas()

    # Verificar si la matriz tiene más elementos que números posibles sin repetición
    if n * m > len(data):
        print(
            "No es posible generar una matriz sin repeticiones con los parámetros proporcionados."
        )
        return []

    claves = list(data.keys())

    while True:
        matriz = np.random.choice(claves, size=(n, m), replace=False)
        if not any(np.array_equal(matriz, guardada) for guardada in matrices_guardadas):
            guardar_matriz(matriz)
            break

    return matriz


def guardar_matriz(matriz):
    with open("matrices_guardadas.json", "a", encoding="utf-8") as archivo:
        json.dump(matriz.tolist(), archivo, ensure_ascii=False)
        archivo.write("\n")


def cargar_matrices_guardadas():
    matrices = []
    try:
        with open("matrices_guardadas.json", "r") as archivo:
            for linea in archivo:
                matriz = json.loads(linea)
                matrices.append(matriz)
    except FileNotFoundError:
        pass
    return matrices


def generar_tablas(size: int, num_tables: int):
    for _ in range(num_tables):
        tabla = generar_matriz_aleatoria(size, size)
        mostrar_tabla(tabla)
        print("\n")
    return True


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Generador de tablas de lotería")
    size = [0]
    num_tables = [0]

    def start_generation():
        size[0] = int(size_entry.get())
        num_tables[0] = int(num_tables_entry.get())
        root.destroy()

    size_label = tk.Label(root, text="Tamaño de la tabla:")
    size_label.pack()

    size_entry = tk.Entry(root)
    size_entry.pack()

    num_tables_label = tk.Label(root, text="Cantidad de tablas a generar:")
    num_tables_label.pack()

    num_tables_entry = tk.Entry(root)
    num_tables_entry.pack()

    start_button = tk.Button(root, text="Comenzar generación", command=start_generation)
    start_button.pack()
    center_window(root)
    root.mainloop()

    if size[0] > 0 and num_tables[0] > 0:
        generar_tablas(size[0], num_tables[0])
