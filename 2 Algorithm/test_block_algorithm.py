import unittest
from block_algorithm import solve_blocks

class TestSolveBlocks(unittest.TestCase):
    """Pruebas para la función solve_blocks."""

    def test_caso_estandar(self):
        """Prueba el caso estándar proporcionado en el reto."""
        input_array = [1, 3, 2, 0, 7, 8, 1, 3, 0, 6, 7, 1]
        self.assertEqual(solve_blocks(input_array), "123 1378 167")

    def test_bloques_vacios(self):
        """Prueba que los bloques vacíos se convierten en 'X'."""
        input_array = [2, 1, 0, 0, 3, 4]
        self.assertEqual(solve_blocks(input_array), "12 X 34")

    def test_cero_al_final(self):
        """Prueba que un cero al final crea un bloque 'X'."""
        input_array = [3, 1, 0]
        self.assertEqual(solve_blocks(input_array), "13 X")