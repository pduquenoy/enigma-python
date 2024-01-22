from string import ascii_lowercase
import logging
import unittest

class Enigma:
    
    plugboard = None
    rotors = None
    reflector = None
    etw = None

    alphabet = list(ascii_lowercase)

    def __init__(self, plugboard, rotors, reflector,etw):
        self.plugboard = plugboard
        self.rotors = rotors
        self.reflector = reflector
        self.etw = etw
    

    def input_char(self,char):
        logging.debug("Input char: {}".format(char))
        return self.process_char(char)

    def process_char(self, char):
        scrambled_char = self.plugboard.switch_char(char)
        logging.debug("Scrambled letter from plugboard: {}".format(scrambled_char))
        iteration = 0
        for rotor in self.rotors:
            if iteration == 0:
                scrambled_char = rotor.scramble_letter_index(rotor.wiring,Enigma.alphabet.index(scrambled_char))
            else:
                scrambled_char = rotor.scramble_letter_index(rotor.wiring,Enigma.alphabet.index(scrambled_char)-self.rotors[iteration-1].position) 
            iteration +=1
            logging.debug("Scrambled letter from rotor{}: {}".format(str(iteration),scrambled_char))
        scrambled_char = self.reflector.scramble_letter_index(self.reflector.wiring,(Enigma.alphabet.index(scrambled_char)-self.rotors[iteration-1].position))
        logging.debug("Scrambled letter from reflector: {}".format(scrambled_char))
        for rotor in reversed(self.rotors):
            if iteration == len(self.rotors):
                scrambled_char = rotor.scramble_letter_index(Enigma.alphabet,(rotor.wiring.index(Enigma.shift_letter(scrambled_char,rotor.position))-rotor.position))
            else:
                scrambled_char = rotor.scramble_letter_index(Enigma.alphabet,(rotor.wiring.index(Enigma.shift_letter(scrambled_char, (rotor.position - self.rotors[iteration].position))) - rotor.position))
            iteration -=1
            logging.debug("Scrambled letter from rotor{}: {}".format(str(iteration+1),scrambled_char))   
        scrambled_char = self.etw.switch_char(scrambled_char,-self.rotors[iteration].position)
        
       
        logging.debug("Scrambled letter from ETW: {}".format(scrambled_char))
        logging.info("Scrambled letter to lamp: {}".format(scrambled_char))
        return scrambled_char
    
    @staticmethod        
    def shift_letter(letter,shift):
	    return Enigma.alphabet[(Enigma.alphabet.index(letter)+shift) % len(Enigma.alphabet)]

