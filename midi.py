'''
    MIDI class: translates pygame.midi messages to waves
'''
from wave import Wave
from pygame import midi

class Midi:

    def __init__(self, event):
        data_bytes, self.timestamp = event
        self.status, self.data1, self.data2, self.data3 = data_bytes

    def generate_wave(self):
        return Wave(midi.midi_to_frequency(self.data1),
                    vol=self.data2 / 127)

class MidiList:

    def __init__(self, event_list):
        self.midi_events = []
        for e in event_list:
            self.midi_events.append(Midi(e))

    def generate_wave_list(self):
        waves = [] # list of waves

        for e in self.midi_events:
            if e.status == 144: # press event
                start_time = e.timestamp
                end_time = next(x for x in self.midi_events 
                        if x.status == 128
                        and x.data1 == e.data1).timestamp
                duration = (end_time - start_time) / 1000 # from ms to s
                frequency = midi.midi_to_frequency(e.data1)
                velocity = e.data2 / 127 # vel ranges from 1 to 127

                waves.append(Wave(frequency, dur=duration, vol=velocity))

        return waves
