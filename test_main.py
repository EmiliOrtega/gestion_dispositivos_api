import unittest
from main import crear_dispositivo, listar_dispositivos, actualizar_dispositivo, eliminar_dispositivo

class TestAPI(unittest.TestCase):

    def test_crear(self):
        r = crear_dispositivo("Test", "Tester")
        self.assertIsInstance(r, dict)  # ahora validas tipo, no status_code
        self.assertIn("id", r)

    def test_listar(self):
        r = listar_dispositivos()
        self.assertIsInstance(r, list)  # ahora validas tipo lista
        self.assertGreater(len(r), 0)

    def test_actualizar(self):
        r = actualizar_dispositivo(1, "Actualizado", "Editado")
        self.assertIsInstance(r, dict)
        self.assertEqual(r.get("name"), "Actualizado")

    def test_eliminar(self):
        r = eliminar_dispositivo(3)
        self.assertTrue(r)  # porque tu función devuelve True si lo logra
