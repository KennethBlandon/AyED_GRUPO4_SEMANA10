class RecetaMedica:

    MEDICAMENTOS_PREDETERMINADOS = ["paracetamol", "emesis", "diazepam"]
    DOSIS_PREDETERMINADAS = ["5 x dia", "2 x semana", "1 x dia"]

    def __init__(self, medicamentos=None, dosis=None):
        self.medicamentos = RecetaMedica.MEDICAMENTOS_PREDETERMINADOS
        self.dosis = RecetaMedica.DOSIS_PREDETERMINADAS
        if len(self.medicamentos) != len(self.dosis):
            raise ValueError("La cantidad de medicamentos debe coincidir con la cantidad de dosis.")

    def __repr__(self):
        items = [
            f"{med} ({dos})"
            for med, dos in zip(self.medicamentos, self.dosis)
        ]
        return f"RecetaMedica({', '.join(items)})"

    @staticmethod
    def añadir_receta_lista(lista_recetas: list, medicamentos=None, dosis=None):
        receta = RecetaMedica(medicamentos, dosis)
        lista_recetas.append(receta)
