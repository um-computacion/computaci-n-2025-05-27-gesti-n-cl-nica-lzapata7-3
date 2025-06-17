import unittest
from src.models.medico import Medico
from src.models.especialidad import Especialidad 
from src.models.excepciones import ( NombreInvalidoError,MatriculaInvalidaError,EspecialidadVaciaError,EspecialidadDuplicadaError)

class TestMedico(unittest.TestCase):

    def setUp(self):
        self.pediatria = Especialidad("Pediatría", ["lunes", "miércoles"])
        self.cardiologia = Especialidad("Cardiología", ["martes", "jueves"])
        self.dermatologia = Especialidad("Dermatología", ["viernes"])
        self.neurologia = Especialidad("Neurología", ["Martes", "Viernes"])

    

    def test_crear_medico_funciona_bien_con_una_especialidad(self):
        medico_basico = Medico("Dr. Marcos Garcíia", "MP45678", [self.pediatria])
        self.assertIsNotNone(medico_basico) 
        self.assertEqual(medico_basico.obtener_nombre(), "Dr. Marcos Garcíia")
        self.assertEqual(medico_basico.obtener_matricula(), "MP45678")
        self.assertEqual(len(medico_basico.obtener_especialidad()), 1)
        self.assertIn(self.pediatria, medico_basico.obtener_especialidad())

    def test_crear_medico_funciona_bien_con_varias_especialidades(self):
        medico_completo = Medico("Dra. Julieta Paz", "MP98765", [self.pediatria, self.cardiologia, self.dermatologia])
        self.assertEqual(len(medico_completo.obtener_especialidad()), 3)
        self.assertIn(self.pediatria, medico_completo.obtener_especialidad())
        self.assertIn(self.cardiologia, medico_completo.obtener_especialidad())
        self.assertIn(self.dermatologia, medico_completo.obtener_especialidad())

    

    def test_crear_medico_con_nombre_vacio_o_blanco(self):
        with self.assertRaises(NombreInvalidoError):
            Medico("", "MP11111", [self.pediatria]) 
        with self.assertRaises(NombreInvalidoError):
            Medico("   ", "MP22222", [self.cardiologia]) 

    def test_crear_medico_con_matricula_vacia_o_blanca(self):
        with self.assertRaises(MatriculaInvalidaError):
            Medico("Dr. Sin Matrícula", "", [self.pediatria]) 
        with self.assertRaises(MatriculaInvalidaError):
            Medico("Dra. Sin Matrícula 2", "  ", [self.dermatologia]) 

    def test_crear_medico_sin_especialidades_iniciales(self):
        with self.assertRaises(EspecialidadVaciaError):
            Medico("Dr. Nadie", "MP33333", []) 
        with self.assertRaises(EspecialidadVaciaError):
            Medico("Dra. Nadie Mas", "MP44444", None) 

    def test_crear_medico_con_especialidades_duplicadas_al_inicio(self):
        with self.assertRaises(EspecialidadDuplicadaError):
            Medico("Dr. Doble", "MP55555", [self.pediatria, self.pediatria]) 
        pediatria_mayus = Especialidad("PEDIATRÍA", ["lunes"]) 
        with self.assertRaises(EspecialidadDuplicadaError):
            Medico("Dra. Doble Mayus", "MP66666", [self.pediatria, pediatria_mayus])

    def test_crear_medico_con_algo_que_no_es_especialidad(self):
        with self.assertRaises(TypeError):
            Medico("Dr. Tipo Mal", "MP77777", [self.pediatria, "esto no es una especialidad"])
        with self.assertRaises(TypeError):
            Medico("Dra. Tipo Mal 2", "MP88888", [123, self.cardiologia])

    

    def test_agregar_especialidad_nueva_funciona(self):
        med = Medico("Dr. Agregador", "MP99999", [self.pediatria])
        cantidad_antes = len(med.obtener_especialidad())
        med.agregar_especialidad(self.dermatologia) 
        self.assertEqual(len(med.obtener_especialidad()), cantidad_antes + 1) 
        self.assertIn(self.dermatologia, med.obtener_especialidad()) 

    def test_agregar_especialidad_existente(self):
        med = Medico("Dra. AntiDuplicados", "MP00001", [self.cardiologia])
        with self.assertRaises(EspecialidadDuplicadaError):
            med.agregar_especialidad(self.cardiologia) 
        cardiologia_mayus = Especialidad("CARDIOLOGÍA", ["jueves"])  
        with self.assertRaises(EspecialidadDuplicadaError):
            med.agregar_especialidad(cardiologia_mayus)

    def test_agregar_algo_que_no_es_especialidad(self):
        med = Medico("Dr. NoEntiende", "MP00002", [self.pediatria])
        with self.assertRaises(TypeError):
            med.agregar_especialidad("cadena de texto") 
        with self.assertRaises(TypeError):
            med.agregar_especialidad(999) 

   

    def test_obtener_especialidad_para_dia_que_atiende_devuelve_nombre_correcto(self):
        
        med = Medico("Dr. Buscador", "MP00003", [self.pediatria, self.dermatologia])
        
        self.assertEqual(med.obtener_especialidad_para_dia("lunes"), "Pediatría")
        self.assertEqual(med.obtener_especialidad_para_dia("VIERNES"), "Dermatología") 
        self.assertEqual(med.obtener_especialidad_para_dia("  miércoles  "), "Pediatría")

    def test_obtener_especialidad_para_dia_que_no_atiende_devuelve_none(self):
        
        med = Medico("Dra. Libre", "MP00004", [self.cardiologia]) 
        
        self.assertIsNone(med.obtener_especialidad_para_dia("lunes"))
        self.assertIsNone(med.obtener_especialidad_para_dia("domingo"))
        self.assertIsNone(med.obtener_especialidad_para_dia("")) 

   

    def test_str_formato_de_salida_es_el_esperado(self):
        med_para_str = Medico("Dra. Imprimible", "MP00005", [self.cardiologia, self.neurologia])
        expected_lines = [
            "Dra. Imprimible,",
            "MP00005,",
            "  Cardiología (Días: Jueves, Martes)",
            "  Neurología (Días: Martes, Viernes)"
        ]
        for line in expected_lines:
            self.assertIn(line, str(med_para_str))


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)