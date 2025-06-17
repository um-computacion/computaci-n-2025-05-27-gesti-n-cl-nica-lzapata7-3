from datetime import datetime
from .paciente import Paciente 
from .medico import Medico 
import locale
locale.setlocale(locale.LC_TIME, 'C')    

class Turno:
    def __init__(self, el_paciente, el_medico, fecha_y_hora, la_especialidad):
        self.__paciente = None
        self.__medico = None
        self.__fecha_hora = None
        self.__especialidad = ""

        if not isinstance(el_paciente, Paciente):
            raise TypeError("¡Error! El 'paciente' debe ser un objeto de la clase Paciente.")
        self.__paciente = el_paciente 

        if not isinstance(el_medico, Medico):
            raise TypeError("¡Error! El 'médico' debe ser un objeto de la clase Medico.")
        self.__medico = el_medico 

        if not isinstance(fecha_y_hora, datetime):
            raise TypeError("¡Atención! La 'fecha_hora' debe ser un objeto de tipo datetime.")
        self.__fecha_hora = fecha_y_hora 

        if not isinstance(la_especialidad, str) or not la_especialidad.strip():
            raise ValueError("¡La especialidad del turno no puede estar vacía o no ser texto!")
        self.__especialidad = la_especialidad.strip() 


    def obtener_paciente(self):
       
        return self.__paciente

    def obtener_medico(self):
       
        return self.__medico

    def obtener_fecha_hora(self):
        
        return self.__fecha_hora
    
    def obtener_especialidad(self):
       
        dia = self.__fecha_hora.strftime("%A").capitalize()

        
        if self.__medico.atiende_especialidad(self.__especialidad, dia):
            return self.__especialidad



   

    def __str__(self):
        
        fecha_hora_formateada = self.__fecha_hora.strftime("%Y-%m-%d %H:%M")
        return (f"--- Detalles del Turno ---\n"
                f"Paciente: {self.__paciente.obtener_nombre()} (DNI: {self.__paciente.obtener_dni()})\n"
                f"Médico: {self.__medico.obtener_nombre()} (Matrícula: {self.__medico.obtener_matricula()})\n"
                f"Especialidad: {self.__especialidad}\n"
                f"Fecha y Hora: {fecha_hora_formateada}\n"
                f"--------------------------")