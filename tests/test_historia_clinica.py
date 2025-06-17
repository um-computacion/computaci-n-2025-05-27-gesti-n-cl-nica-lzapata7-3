import unittest
from datetime import datetime, timedelta 
from src.models.historia_clinica import HistoriaClinica
from src.models.paciente import Paciente 
from src.models.medico import Medico
from src.models.especialidad import Especialidad
from src.models.turno import Turno
from src.models.receta import Receta


class TestHistoriaClinica(unittest.TestCase):


    def setUp(self):
        self.pediatria = Especialidad("Pediatría", ["lunes", "miércoles"])
        self.cardiologia = Especialidad("Cardiología", ["martes"])
        self.dermatologia = Especialidad("Dermatología", ["viernes"])
        self.paciente_titular = Paciente("Juan Pérez", "12345678", "15/05/1990")
        self.medico_uno = Medico("Dr. Carlos Ruiz", "MP001", [self.pediatria])
        self.medico_dos = Medico("Dra. Laura Soto", "MP002", [self.cardiologia, self.dermatologia])
        self.turno_pediatria = Turno(self.paciente_titular, self.medico_uno, datetime(2025, 6, 16, 9, 0), "Pediatría") 
        self.turno_cardiologia = Turno(self.paciente_titular, self.medico_dos, datetime(2025, 6, 17, 10, 30), "Cardiología") 
        self.receta_uno = Receta(self.paciente_titular, self.medico_uno, ["Paracetamol 500mg"])
        self.receta_dos = Receta(self.paciente_titular, self.medico_dos, ["Ibuprofeno 600mg", "Crema dérmica"])
        
   

    def test_crear_historia_clinica_con_paciente_valido(self):
       
        hc = HistoriaClinica(self.paciente_titular)
        self.assertIsNotNone(hc)
        self.assertEqual(hc.obtener_paciente(), self.paciente_titular)
        self.assertEqual(len(hc.obtener_turnos()), 0)
        self.assertEqual(len(hc.obtener_recetas()), 0)

    def test_crear_historia_clinica_con_paciente_invalido(self):
        
        with self.assertRaises(TypeError):
            HistoriaClinica("Esto no es un paciente")
        with self.assertRaises(TypeError):
            HistoriaClinica(None)

   

    def test_agregar_turnos_y_recetas_validas(self):
        
        hc = HistoriaClinica(self.paciente_titular)
        
        hc.agregar_turno(self.turno_pediatria)
        hc.agregar_receta(self.receta_uno)
        hc.agregar_turno(self.turno_cardiologia)
        hc.agregar_receta(self.receta_dos)
        
        self.assertEqual(len(hc.obtener_turnos()), 2)
        self.assertIn(self.turno_pediatria, hc.obtener_turnos())
        self.assertIn(self.turno_cardiologia, hc.obtener_turnos())
        
        self.assertEqual(len(hc.obtener_recetas()), 2)
        self.assertIn(self.receta_uno, hc.obtener_recetas())
        self.assertIn(self.receta_dos, hc.obtener_recetas())

    def test_agregar_objetos_invalidos(self):
       
        hc = HistoriaClinica(self.paciente_titular)
        
        with self.assertRaises(TypeError):
            hc.agregar_turno("no es turno")
        with self.assertRaises(TypeError):
            hc.agregar_turno(None)
        
        with self.assertRaises(TypeError):
            hc.agregar_receta("no es receta")
        with self.assertRaises(TypeError):
            hc.agregar_receta(None)
        
        self.assertEqual(len(hc.obtener_turnos()), 0) 
        self.assertEqual(len(hc.obtener_recetas()), 0)

    

    def test_obtener_turnos_y_recetas_devuelven_copias(self):
        
        hc = HistoriaClinica(self.paciente_titular)
        hc.agregar_turno(self.turno_pediatria)
        hc.agregar_receta(self.receta_uno)
        
        turnos_obtenidos = hc.obtener_turnos()
        recetas_obtenidas = hc.obtener_recetas()
        
        turnos_obtenidos.append(self.turno_cardiologia)
        recetas_obtenidas.append(self.receta_dos)     
        
        self.assertEqual(len(hc.obtener_turnos()), 1) 
        self.assertEqual(len(hc.obtener_recetas()), 1) 
        self.assertNotIn(self.turno_cardiologia, hc.obtener_turnos())
        self.assertNotIn(self.receta_dos, hc.obtener_recetas())

    

    def test_str_muestra_formato_correcto(self):
        self.maxDiff = None

        hc = HistoriaClinica(self.paciente_titular)
        hc.agregar_turno(self.turno_pediatria)
        hc.agregar_receta(self.receta_uno)

        
        fecha_receta_formateada = self.receta_uno._Receta__fecha.strftime("%Y-%m-%d %H:%M:%S")

        expected_output = (
            "--- Historia Clínica ---\n"
            "Paciente: Juan Pérez (DNI: 12345678)\n"
            "  Turnos:\n[\n"
            "    --- Detalles del Turno ---,\n"
            "    Paciente: Juan Pérez (DNI: 12345678),\n"
            "    Médico: Dr. Carlos Ruiz (Matrícula: MP001),\n"
            "    Especialidad: Pediatría,\n"
            "    Fecha y Hora: 2025-06-16 09:00,\n"
            "    --------------------------\n"
            "  ]\n"
            "  Recetas:\n[\n"
            "    Receta(,\n"
            f"      Paciente: Juan Pérez (DNI: 12345678),\n"
            f"      Médico: Dr. Carlos Ruiz (Matrícula: MP001),\n"
            f"      Medicamentos: [Paracetamol 500mg],\n"
            f"      Fecha de Emisión: {fecha_receta_formateada},\n"
            f"    )\n"
            "  ]\n"
            "-------------------------"
        )

    def test_str_con_listas_de_elementos_vacios(self):
        
       
        hc_vacia = HistoriaClinica(self.paciente_titular)
        expected_output_vacia = (
            "--- Historia Clínica ---\n"
            "Paciente: Juan Pérez (DNI: 12345678)\n"
            "  Turnos: [] (Este paciente no tiene turnos registrados aún)\n"
            "  Recetas: [] (Este paciente no tiene recetas registradas aún)\n"
            "-------------------------"
        )
        self.assertEqual(str(hc_vacia), expected_output_vacia)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)