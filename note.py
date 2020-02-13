'''
    Note class
'''

import math

NOTES = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']

class Note:

    def __init__(self, note, octave = 4):
        if note not in NOTES:
            print('Note must be c, c#, d, d#, e, f, f#, g, g#')
        else:
            self.note = note.strip().lower()
            self.octave = octave
            self.index = NOTES.index(self.note)

    def transpose(self, halfsteps):
        self.octave = self.octave + math.floor((self.index + halfsteps) / 12)
        self.index = self.index + (halfsteps%12)
        self.note = NOTES[self.index]

    def octave_shift(self, octave_steps):
        self.transpose(12 * octave_steps)

    def frequency(self):
        c0_freq = 16.35159783128741
        return c0_freq * (2 ** (float(self.index) / 12.0)) * (2 ** self.octave)

