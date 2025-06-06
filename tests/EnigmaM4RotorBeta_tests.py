
from enigmapython.EnigmaM4RotorBeta import EnigmaM4RotorBeta
from string import ascii_lowercase
import unittest

class TestEnigmaM4RotorBeta(unittest.TestCase):
    
    def test_scramble_char_a_position_0(self):
        rotor = EnigmaM4RotorBeta(0)
        char = "a"
        scrambled_char = rotor.scramble_char(rotor.wiring,list(ascii_lowercase).index(char),0)
        self.assertEqual(scrambled_char,"l","Scramble error")

    def test_scramble_char_z_position_0(self):
        rotor = EnigmaM4RotorBeta(0)
        char = "z"
        scrambled_char = rotor.scramble_char(rotor.wiring,list(ascii_lowercase).index(char),0)
        self.assertEqual(scrambled_char,"s","Scramble error")

if __name__ == "__main__":
    unittest.main()