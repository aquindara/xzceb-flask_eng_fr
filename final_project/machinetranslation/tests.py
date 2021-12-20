import unittest

from translator import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase): 
    def test_e2f1(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') # test when hello is given as input the output is bonjour.
        self.assertEqual(englishToFrench('0'), '0') # test when null is given as input the output is null.
        

class TestfrenchToEnglish(unittest.TestCase): 
    def test_f2e1(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # test when bonjour is given as input the output is hello.
        self.assertEqual(frenchToEnglish('0'), '0') # test when null is given as input the output is null.
        
unittest.main()