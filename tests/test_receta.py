import unittest
from datetime import datetime, timedelta 
from src.models.receta import Receta
from src.models.paciente import Paciente 
from src.models.medico import Medico
from src.models.especialidad import Especialidad 
from src.models.excepciones import ( NombreInvalidoError, MatriculaInvalidaError, EspecialidadVaciaError)

class TestReceta(unittest.TestCase):

    def setUp(self):

        self.especialidad_general = Especialidad("Medicina General", ["lunes", "miércoles"])


        self.paciente_valido = Paciente("Sofia Ramos", "40567890", "12/06/1995")

        self.medico_valido = Medico("Dra. Laura Flores", "MP23456", [self.especialidad_general])

        self.lista_medicamentos_ok = ["Amoxicilina 500mg", "Ibuprofeno 400mg", "Vitamina C"]
        self.lista_medicamentos_vacia = [] 
        self.lista_medicamentos_con_invalido = ["Paracetamol", "", "Aspirina"]
        self.lista_medicamentos_con_tipo_incorrecto = ["Jarabe", 123, "Pastillas"] 

  

    def test_crear_receta_con_datos_validos_funciona_correctamente(self):
       
        print("\n--- Probando creación de receta exitosa ---")
        receta_ok = Receta(self.paciente_valido, self.medico_valido, self.lista_medicamentos_ok)
       
        self.assertIsNotNone(receta_ok) 
        self.assertEqual(receta_ok._Receta__paciente, self.paciente_valido) 
        self.assertEqual(receta_ok._Receta__medico, self.medico_valido)
        self.assertListEqual(receta_ok._Receta__medicamentos, self.lista_medicamentos_ok)
        
        ahora = datetime.now()
        self.assertTrue(ahora - receta_ok._Receta__fecha < timedelta(seconds=5))
        print("Receta creada con éxito. ¡Fecha y datos correctos!")

    

    def test_crear_receta_con_paciente_invalido(self):

        print("\n--- Probando error: paciente inválido en receta ---")
        with self.assertRaises(TypeError):
            Receta("No soy un paciente", self.medico_valido, self.lista_medicamentos_ok)
        with self.assertRaises(TypeError):
            Receta(None, self.medico_valido, self.lista_medicamentos_ok)
        print("Error de paciente inválido detectado. ¡Bien!")

    def test_crear_receta_con_medico_invalido(self):
    
        print("\n--- Probando error: médico inválido en receta ---")
        with self.assertRaises(TypeError):
            Receta(self.paciente_valido, "No soy un médico", self.lista_medicamentos_ok)
        with self.assertRaises(TypeError):
            Receta(self.paciente_valido, None, self.lista_medicamentos_ok)
        print("Error de médico inválido detectado. ¡Funciona!")

    def test_crear_receta_con_lista_medicamentos_no_lista(self):
        
        print("\n--- Probando error: medicamentos no es una lista ---")
        with self.assertRaises(TypeError):
            Receta(self.paciente_valido, self.medico_valido, "Paracetamol") 
        with self.assertRaises(TypeError):
            Receta(self.paciente_valido, self.medico_valido, None) 
        print("Error de medicamentos que no es lista detectado. ¡Perfecto!")

    def test_crear_receta_con_lista_medicamentos_vacia_lanza_value_error(self):

        print("\n--- Probando error: lista de medicamentos vacía ---")
        with self.assertRaises(ValueError):
            Receta(self.paciente_valido, self.medico_valido, self.lista_medicamentos_vacia)
        print("Error de lista de medicamentos vacía detectado. ¡Exacto!")

    def test_crear_receta_con_medicamento_invalido_en_lista_lanza_value_error(self):
        
        print("\n--- Probando error: medicamento individual inválido en la lista ---")
        with self.assertRaises(ValueError):
            Receta(self.paciente_valido, self.medico_valido, self.lista_medicamentos_con_invalido)
        with self.assertRaises(ValueError):
            Receta(self.paciente_valido, self.medico_valido, self.lista_medicamentos_con_tipo_incorrecto) 
        print("Error de medicamento inválido en lista detectado. ¡Muy bien!")

   

    def test_str_muestra_formato_correcto_de_receta(self):

        print("\n--- Probando el formato de impresión de la receta (__str__) ---")
        fecha_fija_para_str = datetime(2025, 1, 15, 12, 30, 0) 

        receta_para_str = Receta(self.paciente_valido, self.medico_valido, ["Analgesico", "Antihistaminico"])

        fecha_generada_formateada = receta_para_str._Receta__fecha.strftime("%Y-%m-%d %H:%M:%S")
        expected_output = (
            f"Receta(\n"
            f"  Paciente: Sofia Ramos (DNI: 40567890)\n"
            f"  Médico: Dra. Laura Flores (Matrícula: MP23456)\n"
            f"  Medicamentos: [Analgesico, Antihistaminico]\n"
            f"  Fecha de Emisión: {fecha_generada_formateada}\n"
            f")"
        )
        self.assertEqual(str(receta_para_str), expected_output)
        print("Formato de impresión de receta OK. ¡Se ve bien!")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)