class Paciente:
    
    # El modelo contiene el nombre del paciente y el motivo de su consulta

    def __init__(self, nombre: str, motivo_consulta: str):
        self.nombre = nombre
        self.motivo_consulta = motivo_consulta

    def __repr__(self):
        return f"Paciente(nombre='{self.nombre}', motivo_consulta='{self.motivo_consulta}')"

    def añadir_paciente_lista_espera(lista_espera: list, nombre: str, motivo_consulta: str):
        nuevo_paciente = Paciente(nombre, motivo_consulta)
        lista_espera.append(nuevo_paciente)
