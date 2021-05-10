import unittest
import exercise_1


class TestEx1(unittest.TestCase):

    def test_myName(self):
        result = exercise_1.myName("Zed A Shaw")
        self.assertEqual(result, 'Zed A Shaw')

