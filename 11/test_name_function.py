
import unittest
from name_function import get_formated_name

class NamesTestCase(unittest.TestCase):
    """Тесты для 'name_function.py'"""

    def test_first_last_name(self):
        """Имена вида 'Jenis Joplin' работают, правильно!"""
        formatted_name = get_formated_name('jenis', 'joplin')
        self.assertEqual(formatted_name, 'Jenis Joplin')  # Проверяет полученный результат с ожидающим

    def test_first_last_middle_name(self):
        """Работают ли такие имена, как 'Wolfgang Amadeus Mozart'?"""
        formatted_name = get_formated_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__=='__main__':
    unittest.main()