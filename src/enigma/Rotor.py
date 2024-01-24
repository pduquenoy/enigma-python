from Observable import Observable
from string import ascii_lowercase

class Rotor(Observable):
    wiring = None
    position = 0
    rotations_counter = 0
    notch_indexes = None

    def reset_position(self):
        self.position = 0
    
    def increment_position(self):
        self.position = ((self.position + 1) % len(self.wiring))
        self.rotations_counter = ((self.rotations_counter + 1))   
        for notch_index in self.notch_indexes:
            if (self.position % len(self.wiring)) == notch_index+1:
                self.notify_observers("ciao","ciao")

    def set_position(self,position):
        self.position = position % len(self.wiring)
        self.rotations_counter = 0
        
    def scramble_letter_index(self, dictionary, letter_index):
        scrambled_letter_index_from_rotor = dictionary.index(dictionary[(self.position + letter_index) % len(dictionary)])
        return dictionary[scrambled_letter_index_from_rotor]

    def __init__(self, wiring, position, notch_indexes=[]):
        self.wiring = wiring
        self.position = position % len(wiring)
        self.notch_indexes = notch_indexes

    def __str__(self):
        pointer = ' ' * self.position + '^'
        return self.wiring + '\n' + pointer 
    
