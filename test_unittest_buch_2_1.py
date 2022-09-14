import unittest
import buch_2_1

document = [
             {"type":"type 1","number":"number 1",
             "name": "name 1"},
             {"type":"type 2","number":"number 2",
             "name":"name 2"}
]
directories = {
        '1': ['number 1'],
        '2': ['number 2'],
        '3': []
}

class TestSomething(unittest.TestCase):
    def setUp(self):
        print("method setUp")
        
    def tearDown(self):
        print("method tearDown")
        
    def test_f_people(self):
        print('test1')
        self.assertEqual(buch_2_1.f_people(document, 'number 1'), 'name 1')
        
    def test_f_shelf(self):
        print('test2')
        self.assertEqual(buch_2_1.f_shelf(directories, 'number 1'), '1 полка')
        
    def test_f_list(self):
        print('test3')
        self.assertEqual(buch_2_1.f_list(document), True)
        
    def test_f_list_shelf(self):
        print('test4')
        self.assertEqual(buch_2_1.f_list_shelf(directories), True)
       
    def test_f_add_(self):
        print('test5')
        self.assertEqual(buch_2_1.f_add(document,directories,'type_new','number_new','name_new','1'), True)


if __name__ == '__main__':
    unittest.main()
    
