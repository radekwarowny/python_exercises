import unittest
import codewars

class TestCodewars(unittest.TestCase):

    # Challenge 1
    def test_challenge1(self):
        self.assertEqual(codewars.challenge1(10), 23)
        self.assertEqual(codewars.challenge1(12), 33)
        self.assertEqual(codewars.challenge1(13), 45)


    # Challenge 2
    def test_is_pangram(self):
        pangram = "ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"
        self.assertTrue(codewars.is_pangram(pangram))
        self.assertFalse(codewars.is_pangram("Radek"))


    # Challenge 5
    def test_domain_name(self):
        self.assertEqual(codewars.domain_name("http://google.com"), "google")
        self.assertEqual(codewars.domain_name("http://google.co.jp"), "google")
        self.assertEqual(codewars.domain_name("www.xakep.ru"), "xakep")
        self.assertEqual(codewars.domain_name("https://youtube.com"), "youtube")
       

    



if __name__ == '__main__':
    unittest.main()

