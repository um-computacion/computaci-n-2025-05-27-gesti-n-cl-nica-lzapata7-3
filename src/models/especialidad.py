from .excepciones import (TipoEspecialidadInvalidoError,DiasAtencionInvalidosError)

class Especialidad:

    DIAS_VALIDOS_PARA_ATENCION = ["lunes", "martes", "miércoles", "miercoles", "jueves", "viernes", "sábado", "sabado", "domingo"]

    def __init__(self, tipo, dias_atencion):
        self.__tipo = ""
        self.__dias = []

      
        if not tipo or tipo.strip() == "":
            raise TipoEspecialidadInvalidoError("El nombre de la especialidad no puede estar vacío.")
        self.__tipo = tipo.strip().capitalize() 

        
        if not dias_atencion or len(dias_atencion) == 0:
            raise DiasAtencionInvalidosError("Una especialidad tiene que tener días de atención.")
        
        dias_limpios_y_validos = []
        for d in dias_atencion:
            dia_temp = d.strip().lower() 
            if dia_temp not in self.DIAS_VALIDOS_PARA_ATENCION:
                raise DiasAtencionInvalidosError(f"El día '{d}' no es un día válido de la semana.")
           
            if dia_temp not in dias_limpios_y_validos:
                dias_limpios_y_validos.append(dia_temp)
        
        self.__dias = sorted(dias_limpios_y_validos)

   
    def obtener_tipo(self): 
        return self.__tipo

   
    def verificar_dia(self, dia_a_chequear):
        dia_normalizado = dia_a_chequear.strip().lower() 
        
        if dia_normalizado in self.__dias: 
            return True
        else:
            return False

   
    def __str__(self):
        
        dias_formateados = []
        for dia in self.__dias:
            dias_formateados.append(dia.capitalize())

        
        texto_dias = ", ".join(dias_formateados)
        return f"{self.__tipo} (Días: {texto_dias})"

    
    def __eq__(self, other):
        if not isinstance(other, Especialidad): 
            return NotImplemented
        return self.__tipo.lower() == other.__tipo.lower() 

    
    def __hash__(self):
        return hash(self.__tipo.lower())
    
    def obtener_dias_atencion(self):
        return self.__dias