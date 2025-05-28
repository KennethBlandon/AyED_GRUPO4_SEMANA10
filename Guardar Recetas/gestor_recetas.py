from collections import deque

class Recetario:
    def __init__(self):
        self.recetas = deque()

    def agregar_receta(self, receta):
        self.recetas.append(receta)

    def obtener_proxima_receta(self):
        return self.recetas.popleft() if self.recetas else None

    def mostrar_recetas(self):
        return list(self.recetas)
