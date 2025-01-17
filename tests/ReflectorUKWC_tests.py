
from enigmapython.ReflectorUKWC import ReflectorUKWC
from string import ascii_lowercase
import unittest

class TestReflectorUKWC(unittest.TestCase):
    
    def test_reflector_b_scramble_char_z(self):
        reflector = ReflectorUKWC()
        char = "z"
        scrambled_char = reflector.scramble_char(reflector.wiring,list(ascii_lowercase).index(char),0)
        self.assertEqual(scrambled_char,"l","Scramble error")

if __name__ == "__main__":
    unittest.main()