import unittest
from unittest.mock import patch, MagicMock
import database
from mysql.connector import Error as MySQLError

class TestAddFiltersFunction(unittest.TestCase):
    """Pruebas específicas para la función de ayuda 'add_filters_to_query'."""

    def test_sin_filtros(self):
        """Debe devolver un string vacío y una lista vacía si no hay filtros."""
        query, params = database.add_filters_to_query({})
        self.assertEqual(query, "")
        self.assertEqual(params, [])

    def test_con_un_filtro(self):
        """Debe construir la consulta y los parámetros para un filtro."""
        query, params = database.add_filters_to_query({'city': 'bogota'})
        self.assertEqual(query, " AND p.city = %s")
        self.assertEqual(params, ['bogota'])

    def test_con_multiples_filtros(self):
        """Debe construir la consulta y los parámetros para múltiples filtros."""
        filters = {'city': 'medellin', 'year': '2020'}
        query, params = database.add_filters_to_query(filters)
        self.assertEqual(query, " AND p.city = %s AND p.year = %s")
        self.assertEqual(params, ['medellin', '2020'])


class TestGetPropertiesFunction(unittest.TestCase):
    """Pruebas para la función principal 'get_properties'."""

    @patch('database.mysql.connector.connect')
    def test_llamada_correcta_a_execute(self, mock_connect):
        """Verifica que cursor.execute se llama con la consulta y los parámetros correctos."""
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        
        filters = {'city': 'bogota'}
        database.get_properties(filters)

        expected_query = database.BASE_QUERY + " AND p.city = %s"
        expected_params = ('bogota',)

        mock_cursor.execute.assert_called_once_with(expected_query, expected_params)

    @patch('database.mysql.connector.connect')
    def test_manejo_de_error_conexion(self, mock_connect):
        """Prueba que la función devuelve None si la conexión a la BD falla."""
        mock_connect.side_effect = MySQLError("Fallo simulado")
        resultado = database.get_properties({})
        self.assertIsNone(resultado)