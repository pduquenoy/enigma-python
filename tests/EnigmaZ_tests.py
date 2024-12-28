from enigmapython.EnigmaZRotorI import EnigmaZRotorI
from enigmapython.EnigmaZRotorII import EnigmaZRotorII
from enigmapython.EnigmaZRotorIII import EnigmaZRotorIII
from enigmapython.EnigmaZEtw import EnigmaZEtw
from enigmapython.EnigmaZ import EnigmaZ
from enigmapython.ReflectorZUKW import ReflectorZUKW
import unittest


class TestEnigmaZ(unittest.TestCase):
    def test_enigma_Z_rotors_I_I_I_small_number(self):
        rotor1 = EnigmaZRotorI()
        rotor2 = EnigmaZRotorI()
        rotor3 = EnigmaZRotorI()
        reflector = ReflectorZUKW()
        etw = EnigmaZEtw()
        enigma = EnigmaZ(rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = '23041981'
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,"95539350","Enigma encryption error")

    def test_enigma_Z_rotors_I_I_I_medium_number(self):
        rotor1 = EnigmaZRotorI()
        rotor2 = EnigmaZRotorI()
        rotor3 = EnigmaZRotorI()
        reflector = ReflectorZUKW()
        etw = EnigmaZEtw()
        enigma = EnigmaZ(rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = '123456789012345678901234567890'
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,"719365648926063110712103315478","Enigma encryption error")

    def test_enigma_Z_rotors_I_I_I_long_number(self):
        rotor1 = EnigmaZRotorI()
        rotor2 = EnigmaZRotorI()
        rotor3 = EnigmaZRotorI()
        reflector = ReflectorZUKW()
        etw = EnigmaZEtw()
        enigma = EnigmaZ(rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = '123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890'
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,"719365648926063110712103315478649268658141631204469499646181818397946868524735118183979464949864668933966860886892656584097183330649798501019113249431315348841101033134738885954263297682300869728735053657471915365747191328152842322820773753201522423796480416274448080627286517424479718353099666141045251729593457112393330855484216260931117920460020293656481016","Enigma encryption error")

    def test_enigma_Z_rotors_I_I_I_long_long_number(self):
        rotor1 = EnigmaZRotorI()
        rotor2 = EnigmaZRotorI()
        rotor3 = EnigmaZRotorI()
        reflector = ReflectorZUKW()
        etw = EnigmaZEtw()
        enigma = EnigmaZ(rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = '123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890'
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,"719365648926063110712103315478649268658141631204469499646181818397946868524735118183979464949864668933966860886892656584097183330649798501019113249431315348841101033134738885954263297682300869728735053657471915365747191328152842322820773753201522423796480416274448080627286517424479718353099666141045251729593457112393330855484216260931117920460020293656481016997584420868926865886862179544005143531357450542212113285436905944811181839024644851430313710331847320053142714103310478689265658131033134786442002524097183930248207707520520799754982074975774986266879818243634571123933486819313617153428418685240251957966860862609311172097985310866420715258387975961315348841325651942462669171143808595426436514313154347070927","Enigma encryption error")

   
if __name__ == "__main__":
    unittest.main(verbosity=2)