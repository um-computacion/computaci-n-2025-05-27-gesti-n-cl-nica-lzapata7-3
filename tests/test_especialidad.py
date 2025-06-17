import unittest
from src.models.especialidad import Especialidad
from src.models.excepciones import ( TipoEspecialidadInvalidoError,DiasAtencionInvalidosError)

class TestEspecialidad(unittest.TestCase):

    def setUp(self):
       
        self.tipo_valido = "Cardiología"
        self.dias_validos_1 = ["lunes", "miércoles", "viernes"]
        self.dias_validos_2 = ["Martes", "JUEVES"] 
        self.dias_validos_cortos = ["lunes"] 

   

    def test_crear_especialidad_con_datos_correctos_funciona_bien(self):
        
        esp = Especialidad(self.tipo_valido, self.dias_validos_1)
        
        
        self.assertIsNotNone(esp)
        self.assertEqual(esp.obtener_tipo(), "Cardiología")
        self.assertEqual(esp.obtener_dias_atencion(), ["lunes", "miércoles", "viernes"])
        self.assertEqual(len(esp.obtener_dias_atencion()), 3)

    def test_crear_especialidad_con_dias_validos_pero_en_distintas_mayusculas_los_guarda_en_minusculas(self):
        
        esp = Especialidad("Neurología", self.dias_validos_2)
        self.assertEqual(esp.obtener_tipo(), "Neurología")
        self.assertEqual(esp.obtener_dias_atencion(), ["jueves", "martes"]) 

    def test_crear_especialidad_con_dias_duplicados_en_la_lista_inicial_los_guarda_sin_duplicar(self):
        
        dias_con_duplicados = ["lunes", "lunes", "martes", "Martes"]
        esp = Especialidad("Dermatología", dias_con_duplicados)
        self.assertEqual(len(esp.obtener_dias_atencion()), 2)
        self.assertIn("lunes", esp.obtener_dias_atencion())
        self.assertIn("martes", esp.obtener_dias_atencion())

    

    def test_crear_especialidad_con_nombre_vacio_lanza_error(self):
        
        with self.assertRaises(TipoEspecialidadInvalidoError):
            Especialidad("", self.dias_validos_1)
        
        with self.assertRaises(TipoEspecialidadInvalidoError):
            Especialidad("   ", self.dias_validos_1) 

    def test_crear_especialidad_sin_dias_de_atencion_lanza_error(self):
       
        with self.assertRaises(DiasAtencionInvalidosError):
            Especialidad(self.tipo_valido, []) 
        
        with self.assertRaises(DiasAtencionInvalidosError):
            Especialidad(self.tipo_valido, None) 

    def test_crear_especialidad_con_dia_invalido_lanza_error(self):
        
        dias_con_uno_malo = ["lunes", "día raro", "miércoles"]
        with self.assertRaises(DiasAtencionInvalidosError):
            Especialidad(self.tipo_valido, dias_con_uno_malo)
        
        dias_otro_malo = ["23/12/2024"] 
        with self.assertRaises(DiasAtencionInvalidosError):
            Especialidad(self.tipo_valido, dias_otro_malo)

    

    def test_obtener_tipo_devuelve_el_nombre_correcto(self):
        
        esp = Especialidad("Oftalmología", self.dias_validos_1)
        self.assertEqual(esp.obtener_tipo(), "Oftalmología")

  

    def test_verificar_dia_devuelve_true_para_dias_que_si_atiende(self):
       
        esp = Especialidad("Pediatría", ["lunes", "martes"])
        self.assertTrue(esp.verificar_dia("lunes"))
        self.assertTrue(esp.verificar_dia("MARTES")) 
        self.assertTrue(esp.verificar_dia("  lunes  ")) 

    def test_verificar_dia_devuelve_false_para_dias_que_no_atiende(self):
        
        esp = Especialidad("Pediatría", ["lunes", "martes"])
        self.assertFalse(esp.verificar_dia("miércoles"))
        self.assertFalse(esp.verificar_dia("Domingo"))
        self.assertFalse(esp.verificar_dia("   ")) 
        self.assertFalse(esp.verificar_dia("otro día"))

    

    def test_str_especialidad_devuelve_formato_correcto(self):
        
        esp_para_str = Especialidad("Traumatología", ["lunes", "miércoles", "viernes"])
        expected_output = "Traumatología (Días: Lunes, Miércoles, Viernes)" 

        esp_un_dia = Especialidad("Odontología", ["jueves"])
        expected_output_un_dia = "Odontología (Días: Jueves)"
        self.assertEqual(str(esp_un_dia), expected_output_un_dia)

   

    def test_especialidades_con_mismo_tipo_son_iguales_sin_importar_mayusculas(self):
       
        esp1 = Especialidad("Cardiología", ["lunes"])
        esp2 = Especialidad("cardiología", ["martes"]) 
        esp3 = Especialidad("CARDIOLOGÍA", ["miércoles"])
        esp_diferente = Especialidad("Pediatría", ["lunes"])

        self.assertEqual(esp1, esp2)
        self.assertEqual(esp1, esp3)
        self.assertNotEqual(esp1, esp_diferente)

    def test_especialidades_con_mismo_tipo_tienen_mismo_hash(self):
        
        esp1 = Especialidad("Radiología", ["lunes"])
        esp2 = Especialidad("radiología", ["martes"])
        esp_diferente = Especialidad("Cirugía", ["lunes"])

        self.assertEqual(hash(esp1), hash(esp2))
        self.assertNotEqual(hash(esp1), hash(esp_diferente))

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)