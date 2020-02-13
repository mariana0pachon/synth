'''
    Instrument class
'''
from wave import Wave
from sequence import Sequence

class Instrument:

    weight_dict = {
        'pure': [1],
        'organ': [1, 0.2],
        'oboe': [0.5, 1, 0.125, 0.125],
    }

    def __init__(self, sequence, inst_name='pure', wave_shape='sine'):
        self.notes =  Sequence(sequence).generate_note_seq()
        self.inst_name = inst_name
        self.wave_shape = wave_shape

    def generate_wave_list(self):

        wave_list = []

        for n in self.notes:
            if isinstance(n, list): # it's a chord
                # todo: way too many nested loops
                wave_list.append(self.__transform_chord(n))

            else: # single note
                wave_list.append(self.__note_to_inst(n))

        return wave_list

    def __transform_chord(self, chord_note_list):

        inst_wave_list = []
        for n in chord_note_list:
            # transform each note to instrument
            inst_wave_list.append(self.__note_to_inst(n))

        # create chord from already transformed notes
        return inst_wave_list[0].add_waves(inst_wave_list)

    def __note_to_inst(self, note):
        weights = self.weight_dict[self.inst_name]
        harmonics = []
        for i in range(len(weights)):
            harmonics.append(Wave(note.frequency() * (i + 1), shape=self.wave_shape))

        return harmonics[0].add_waves(harmonics, weights)
