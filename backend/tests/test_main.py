import unittest

class TestStringMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('Set up before test suite of TestStringMethods')

    @classmethod
    def tearDownClass(self):
        print('Teardown after test suite of TestStringMethods')

    #run for each test case
    def setUp(self):
        print('Set up before test case') 

    #This is a single test case
    def test_upper(self):
        print("test_upper")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("test_isupper")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print("test_split")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    def tearDown(self):
        print('Teardown after test case')

# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(TestStringMethods('test_upper'))
#     suite.addTest(TestStringMethods('test_isupper'))
#     return suite

if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(suite())
    unittest.main()