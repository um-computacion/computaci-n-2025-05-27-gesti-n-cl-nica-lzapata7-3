import unittest
from datetime import datetime, date
from src.models.turno import Turno
from src.models.paciente import Paciente 
from src.models.medico import Medico
from src.models.especialidad import Especialidad 
from src.models.excepciones import ( NombreInvalidoError, MatriculaInvalidaError, EspecialidadVaciaError,)

class TestTurno(unittest.TestCase):

    def setUp(self):
        self.pediatria = Especialidad("Pediatría", ["lunes", "miércoles"])
        self.cardiologia = Especialidad("Cardiología", ["martes", "jueves"])
        self.dermatologia = Especialidad("Dermatología", ["viernes"])

        self.paciente_ejemplo = Paciente("Julia Fernández", "35789012", "15/05/1990")

        # Médicos de prueba
        self.medico_soto = Medico("Dr. Adrián Soto", "MP98765", [self.pediatria, self.cardiologia])
        self.medico_blanco = Medico("Dra. Belén Blanco", "MP12345", [self.dermatologia])
        self.medico_castro = Medico("Dr. Ernesto Castro", "MP67890", [self.pediatria])

        # Fechas y horas para los turnos
        self.fecha_hora_lunes = datetime(2025, 6, 16, 10, 0) 
        self.fecha_hora_martes = datetime(2025, 6, 17, 11, 30) 
        self.fecha_hora_domingo = datetime(2025, 6, 15, 9, 0) 

    # --- Pruebas de Creación de Turno ---

    def test_crear_turno_con_datos_validos(self):
        
        un_turno = Turno(self.paciente_ejemplo, self.medico_soto, self.fecha_hora_lunes, "Pediatría")
        
        self.assertIsNotNone(un_turno)
        self.assertEqual(un_turno.obtener_paciente(), self.paciente_ejemplo)
        self.assertEqual(un_turno.obtener_medico(), self.medico_soto)
        self.assertEqual(un_turno.obtener_fecha_hora(), self.fecha_hora_lunes)
        self.assertEqual(un_turno.obtener_especialidad(), "Pediatría")

    

    def test_crear_turno_con_datos_invalidos(self):
      
        with self.assertRaises(TypeError):
            Turno("No soy un paciente", self.medico_soto, self.fecha_hora_lunes, "Pediatría")
        with self.assertRaises(TypeError):
            Turno(None, self.medico_soto, self.fecha_hora_lunes, "Pediatría")

       
        with self.assertRaises(TypeError):
            Turno(self.paciente_ejemplo, "No soy un médico", self.fecha_hora_lunes, "Cardiología")
        with self.assertRaises(TypeError):
            Turno(self.paciente_ejemplo, None, self.fecha_hora_lunes, "Cardiología")

        
        with self.assertRaises(TypeError):
            Turno(self.paciente_ejemplo, self.medico_soto, "fecha mala", "Dermatología")
        with self.assertRaises(TypeError):
            Turno(self.paciente_ejemplo, self.medico_soto, None, "Dermatología")

       
        with self.assertRaises(ValueError):
            Turno(self.paciente_ejemplo, self.medico_soto, self.fecha_hora_lunes, "")
        with self.assertRaises(ValueError):
            Turno(self.paciente_ejemplo, self.medico_soto, self.fecha_hora_lunes, "   ")
        with self.assertRaises(ValueError):
            Turno(self.paciente_ejemplo, self.medico_soto, self.fecha_hora_lunes, None)


    def test_medico_atiende_especialidad_y_dia(self):
        turno_a_verificar = Turno(self.paciente_ejemplo, self.medico_soto, self.fecha_hora_lunes, "Pediatría")
        
       
        dia_del_turno_str = turno_a_verificar.obtener_fecha_hora().strftime("%A").capitalize()
        
        especialidad_que_medico_atiende = turno_a_verificar.obtener_medico().obtener_especialidad_para_dia(dia_del_turno_str)
        
        self.assertEqual(especialidad_que_medico_atiende, "Pediatría")  
        self.assertEqual(especialidad_que_medico_atiende, turno_a_verificar.obtener_especialidad())  

    def test_medico_no_atiende_especialidad_o_dia(self):
        
        
        turno_mal_especialidad = Turno(self.paciente_ejemplo, self.medico_blanco, self.fecha_hora_lunes, "Pediatría")
        dia_str = turno_mal_especialidad.obtener_fecha_hora().strftime("%A").lower()
        especialidad_real = turno_mal_especialidad.obtener_medico().obtener_especialidad_para_dia(dia_str)
        self.assertIsNone(especialidad_real) 
        self.assertNotEqual(turno_mal_especialidad.obtener_especialidad(), "Pediatría") 

        
        turno_dia_no_valido = Turno(self.paciente_ejemplo, self.medico_castro, self.fecha_hora_domingo, "Pediatría")
        dia_str = turno_dia_no_valido.obtener_fecha_hora().strftime("%A").lower()
        especialidad_en_ese_dia = turno_dia_no_valido.obtener_medico().obtener_especialidad_para_dia(dia_str)
        self.assertIsNone(especialidad_en_ese_dia) 

   

    def test_devolucion_valores_correctos(self):
        un_turno = Turno(self.paciente_ejemplo, self.medico_soto, self.fecha_hora_martes, "Cardiología")
        self.assertEqual(un_turno.obtener_paciente(), self.paciente_ejemplo)
        self.assertEqual(un_turno.obtener_medico(), self.medico_soto)
        self.assertEqual(un_turno.obtener_fecha_hora(), self.fecha_hora_martes)
        self.assertEqual(un_turno.obtener_especialidad(), "Cardiología")

   

    def test_formato_del_turno(self):
        fecha_para_str = datetime(2025, 7, 20, 15, 45)
        turno_para_imprimir = Turno(self.paciente_ejemplo, self.medico_blanco, fecha_para_str, "Dermatología")
        
        expected_output = (
            "--- Detalles del Turno ---\n"
            "Paciente: Julia Fernández (DNI: 35789012)\n"
            "Médico: Dra. Belén Blanco (Matrícula: MP12345)\n"
            "Especialidad: Dermatología\n"
            "Fecha y Hora: 2025-07-20 15:45\n"
            "--------------------------"
        )
        self.assertEqual(str(turno_para_imprimir), expected_output)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)