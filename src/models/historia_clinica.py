from .paciente import Paciente 
from .turno import Turno       
from .receta import Receta     

class HistoriaClinica:
    def __init__(self, el_paciente):
        self.__paciente = None
        self.__turnos = []   
        self.__recetas = [] 

        if not isinstance(el_paciente, Paciente):
            raise TypeError("¡Ojo! La historia clínica necesita un objeto 'Paciente' real. No me pases otra cosa.")
        self.__paciente = el_paciente

    

    def agregar_turno(self, nuevo_turno):

        
        if not isinstance(nuevo_turno, Turno):
            raise TypeError("¡Error al agregar turno! Solo puedo guardar objetos de tipo 'Turno'.")
        self.__turnos.append(nuevo_turno)

    def agregar_receta(self, nueva_receta):
        

        if not isinstance(nueva_receta, Receta):
            raise TypeError("¡Error al agregar receta! Solo se pueden guardar objetos de tipo 'Receta'.")
        self.__recetas.append(nueva_receta)

    

    def obtener_paciente(self):
        return self.__paciente

    def obtener_turnos(self):
        return self.__turnos[:]

    def obtener_recetas(self):
        return self.__recetas[:]

    

    def __str__(self):
       

        info_paciente = f"Paciente: {self.__paciente.obtener_nombre()} (DNI: {self.__paciente.obtener_dni()})"
        lista_turnos_texto = []
        if self.__turnos:
            for un_turno in self.__turnos:
                lista_turnos_texto.append(str(un_turno))
            
            turnos_formateados = ",\n".join([f"    {linea}" for t_str in lista_turnos_texto for linea in t_str.splitlines()])
            seccion_turnos = f"  Turnos:\n[\n{turnos_formateados}\n  ]"
        else:
            seccion_turnos = "  Turnos: [] (Este paciente no tiene turnos registrados aún)"

        
        lista_recetas_texto = []
        if self.__recetas:
            for una_receta in self.__recetas:
                lista_recetas_texto.append(str(una_receta))
            
            recetas_formateadas = ",\n".join([f"    {linea}" for r_str in lista_recetas_texto for linea in r_str.splitlines()])
            seccion_recetas = f"  Recetas:\n[\n{recetas_formateadas}\n  ]"
        else:
            seccion_recetas = "  Recetas: [] (Este paciente no tiene recetas registradas aún)"
        return (f"--- Historia Clínica ---\n"
                f"{info_paciente}\n"
                f"{seccion_turnos}\n"
                f"{seccion_recetas}\n"
                f"-------------------------")