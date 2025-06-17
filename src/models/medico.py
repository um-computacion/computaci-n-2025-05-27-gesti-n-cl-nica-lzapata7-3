from .especialidad import Especialidad
from .excepciones import (NombreInvalidoError,MatriculaInvalidaError,EspecialidadVaciaError,EspecialidadDuplicadaError)

class Medico:
    def __init__(self, nombre, matricula, especialidades):
        self.__nombre = "" 
        self.__matricula = ""
        self.__especialidades = []

        
        if not nombre or nombre.strip() == "": 
            raise NombreInvalidoError("El nombre del médico no puede estar vacío.")
        self.__nombre = nombre.strip() 

        if not matricula or matricula.strip() == "":
            raise MatriculaInvalidaError("La matrícula del médico no puede estar vacía.")
        self.__matricula = matricula.strip()

       
        if not especialidades: 
            raise EspecialidadVaciaError("Un médico debe tener al menos una especialidad al registrarse.")

        
        for esp in especialidades:
            if not isinstance(esp, Especialidad):
                raise TypeError("Cada elemento de la lista de especialidades debe ser un objeto Especialidad.")
            
            if esp in self.__especialidades:
                raise EspecialidadDuplicadaError(f"Especialidad '{esp.obtener_tipo()}' duplicada en la lista inicial.")
            self.__especialidades.append(esp)


    
    def obtener_nombre(self):
        return self.__nombre

    def obtener_matricula(self):
        return self.__matricula


    def atiende_especialidad(self, especialidad_nombre, dia):
        dia = dia.lower()
        especialidad_nombre = especialidad_nombre.lower()

        for esp in self.__especialidades:
            if (esp.obtener_tipo().lower() == especialidad_nombre and
                dia in [d.lower() for d in esp.obtener_dias_atencion()]):
                return True
        return False

    def agregar_especialidad(self, nueva_especialidad):
        
        if not isinstance(nueva_especialidad, Especialidad):
            raise TypeError("Solo se pueden agregar objetos de tipo Especialidad.")

        
        if nueva_especialidad in self.__especialidades:
            raise EspecialidadDuplicadaError(f"El médico ya tiene la especialidad '{nueva_especialidad.obtener_tipo()}'.")
        
        self.__especialidades.append(nueva_especialidad) 
    
    def obtener_especialidad(self):
        return self.__especialidades


    def obtener_especialidad_para_dia(self, dia):
        
        dia_buscado = dia.strip().lower() 

        for esp in self.__especialidades:
            
            if dia_buscado in esp.obtener_dias_atencion():
                return esp.obtener_tipo() 
        return None 

    
    def __str__(self):
       
        lista_info_especialidades = []
        for esp in self.__especialidades:
            lista_info_especialidades.append(str(esp)) 

        
        especialidades_formateadas = ",\n".join([f"  {info}" for info in lista_info_especialidades])


        return (f"{self.__nombre},\n"
                f"{self.__matricula},\n"
                f"[\n{especialidades_formateadas}\n]")