
import unittest
from traning import name_pet

class NamesPetTestCase(unittest.TestCase):

    # def test_yes_no(self):
    #     yes_no = 

    def test_name_pet(self):
        pet_name = name_pet('rex')
        self.assertEqual(pet_name, 'Rex')


if __name__ in '__main__':
    unittest.main()