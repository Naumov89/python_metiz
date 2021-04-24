
import unittest
from city_functions import city_country

class NameTestCase(unittest.TestCase):

    def test_city_country(self):
        formattet_name = city_country('santiago', 'chili')
        self.assertEqual(formattet_name, 'Santiago, Chili')

    def test_city_country_population(self):
        formatted_name = city_country('santiago', 'chili', 5_000_000)
        self.assertEqual(formatted_name, 'Santiago, Chili - population 5000000')

if __name__ == '__main__':
    unittest.main()