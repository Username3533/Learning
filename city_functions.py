#formats city name and country
import unittest

class Test(unittest.TestCase):

    def test_format_city(self, city, country):
        formatted_name = f'{city}, {country}'
        return formatted_name.title()



    def test_format(self):
        formatted_name = self.test_format_city('aliso', 'california')
        self.assertEqual(formatted_name, 'Aliso, California')



if __name__ == '__main__':
    unittest.main()