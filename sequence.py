'''
    Sequence class
'''
from section import Section

class Sequence:

    def __init__(self, list):
        self.list = list

    def generate_note_seq(self):

        notes = []

        for elt in self.list: # todo: map instead of loop
            notes.append(Section(elt).generate_notes())

        return notes
