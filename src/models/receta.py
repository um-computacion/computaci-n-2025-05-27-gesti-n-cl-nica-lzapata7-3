from datetime import datetime 
from .paciente import Paciente
from .medico import Medico   

class Receta:
    def __init__(self, el_paciente, el_medico, lista_de_medicamentos):
        self.__paciente = None
        self.__medico = None
        self.__medicamentos = []
        self.__fecha = None 

        if not isinstance(el_paciente, Paciente):
            raise TypeError("¡Uy! El 'paciente' que me pasaste no es un objeto de la clase Paciente. Necesito uno válido.")
        self.__paciente = el_paciente

       
        if not isinstance(el_medico, Medico):
            raise TypeError("¡Atención! El 'médico' debe ser un objeto de la clase Medico. ¿Me pasaste otra cosa?")
        self.__medico = el_medico 

     
        if not isinstance(lista_de_medicamentos, list):
            raise TypeError("¡Error! Los 'medicamentos' deben venir en una lista.")
        
        if not lista_de_medicamentos:
            raise ValueError("¡La lista de medicamentos no puede estar vacía! Un médico receta algo, ¿no?")
        
        medicamentos_limpios = [] 
        for med in lista_de_medicamentos:
            if not isinstance(med, str) or not med.strip():
                raise ValueError(f"¡Un medicamento no es válido! '{med}' no es un texto o está vacío. Cada medicamento en la lista debe ser un nombre.")
            medicamentos_limpios.append(med.strip()) 
        
        self.__medicamentos = medicamentos_limpios 
        self.__fecha = datetime.now()
    
    def obtener_medicamentos(self):
        return self.__medicamentos

    def __str__(self):
      
        fecha_formateada = self.__fecha.strftime("%Y-%m-%d %H:%M:%S")
        medicamentos_texto = ", ".join(self.__medicamentos)
        return (f"Receta(\n"
                f"  Paciente: {self.__paciente.obtener_nombre()} (DNI: {self.__paciente.obtener_dni()})\n"
                f"  Médico: {self.__medico.obtener_nombre()} (Matrícula: {self.__medico.obtener_matricula()})\n"
                f"  Medicamentos: [{medicamentos_texto}]\n"
                f"  Fecha de Emisión: {fecha_formateada}\n"
                f")")