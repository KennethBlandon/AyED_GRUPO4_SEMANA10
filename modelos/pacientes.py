class Paciente:
    
    # El modelo contiene el nombre del paciente y el motivo de su consulta

    def __init__(self, nombre: str, motivo_consulta: str):
        self.nombre = nombre
        self.motivo_consulta = motivo_consulta

    def __repr__(self):
        return f"Paciente(nombre='{self.nombre}', motivo_consulta='{self.motivo_consulta}')"