'''
    Section class

    Sequences and Chords are made from Sections
'''

# I don't like this

from note import Note

class Section:

    def __init__(self, sec):
        self.sec = sec

    def __generate_note(self):

        octave = ''.join([i for i in list(self.sec) if i.isdigit()])

        if octave == '':
            octave = '4'

        note = self.sec.replace(octave, '')

        return Note(note, int(octave))

    def __generate_note_list(self):
        string_list = self.sec.strip('[]').split(',')

        note_list = []
        for n in string_list:
            note_list.append(Section(n.strip()).__generate_note())
        return note_list

    def generate_notes(self):

        if '[' in self.sec: # it's a chord
            return self.__generate_note_list()

        return self.__generate_note()
