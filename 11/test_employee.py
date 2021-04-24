
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        first_name = 'Alexander'
        last_name = 'Naumov'
        salary = 3000
        self.my_employee = Employee(first_name, last_name, salary)
        
    def test_give_default_raise(self):
        self.my_employee.give_raise(6000)
        self.assertEqual(9000, self.my_employee.salary)

    def test_show_result(self):
        self.my_employee.show_results()
        self.assertEqual("Alexander Naumov 3000", self.my_employee.show_results())

        
if __name__ == '__main__':
    unittest.main()