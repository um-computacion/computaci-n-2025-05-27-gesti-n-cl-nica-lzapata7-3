import unittest
from src.models.paciente import Paciente
from src.models.excepciones import DNIInvalidoError, NombreInvalidoError, FechaNacimientoInvalidaError
from datetime import datetime, timedelta

class TestPaciente(unittest.TestCase):

    def test_creacion_paciente_valido(self):
        paciente = Paciente("Juan Perez", "12345678", "01/01/1990")
        self.assertEqual(paciente.obtener_dni(), "12345678")
        self.assertEqual(str(paciente), "Juan Perez, 12345678, 01/01/1990")

    def test_dni_correcto(self):
        p = Paciente("Maria Lopez", "87654321", "05/06/1995")
        self.assertEqual(p.obtener_dni(), "87654321")

    def test_str_paciente(self):
        p = Paciente("Carlos Gomez", "11223344", "20/03/1980")
        self.assertEqual(str(p), "Carlos Gomez, 11223344, 20/03/1980")

    def test_nombre_vacio(self):
        with self.assertRaises(NombreInvalidoError):
            Paciente("", "12345678", "01/01/1990")

    def test_nombre_espacios(self):
        with self.assertRaises(NombreInvalidoError):
            Paciente("    ", "12345678", "01/01/1990")

    def test_fecha_formato_invalido(self):
        with self.assertRaises(FechaNacimientoInvalidaError):
            Paciente("Pepe", "12345678", "1990-01-01") 

    def test_fecha_mes_invalido(self):
        with self.assertRaises(FechaNacimientoInvalidaError):
            Paciente("Pepe", "12345678", "01/13/1990")

    def test_fecha_dia_invalido(self):
        with self.assertRaises(FechaNacimientoInvalidaError):
            Paciente("Pepe", "12345678", "32/01/1990")

    def test_fecha_futura(self):
        fecha_futura = datetime.now() + timedelta(days=3)
        fecha_str = fecha_futura.strftime('%d/%m/%Y')
        with self.assertRaises(FechaNacimientoInvalidaError):
            Paciente("Pepe", "12345678", fecha_str)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)