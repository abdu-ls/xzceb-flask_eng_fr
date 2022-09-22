import unittest

from translator import french_to_english, english_to_french

class TestTranslantor(unittest.TestCase):
    def test(self):
        self.assertNotEqual(english_to_french(" "), "Salute")
        self.assertEqual(english_to_french("Hello"), "Bonjour")
     
    def test1(self):
        self.assertNotEqual(french_to_english(" "), "Merci")
        self.assertEqual(french_to_english('Bonjour'), "Hello")
        

    unittest.main()