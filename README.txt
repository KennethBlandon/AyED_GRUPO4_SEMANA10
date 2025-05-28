from collections import deque

class Paciente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial_recetas = []  

    def agregar_receta(self, receta):
        self.historial_recetas.append(receta)  

    def ver_historial(self):
        return self.historial_recetas[::-1]  

cola_espera = deque()

pacientes_registrados = {}


def agregar_paciente(nombre):
    paciente = Paciente(nombre)
    cola_espera.append(paciente)
    pacientes_registrados[nombre] = paciente

def ver_pacientes_en_espera():
    return [paciente.nombre for paciente in cola_espera]

def atender_paciente():
    if cola_espera:
        paciente = cola_espera.popleft()
        receta = input(f"Ingrese la receta para {paciente.nombre}: ")
        paciente.agregar_receta(receta)
        print(f"{paciente.nombre} fue atendido.")
    else:
        print("No hay pacientes en espera.")

def consultar_historial(nombre):
    paciente = pacientes_registrados.get(nombre)
    if paciente:
        historial = paciente.ver_historial()
        for receta in historial:
            print(receta)
    else:
        print("Paciente no encontrado.")
README
