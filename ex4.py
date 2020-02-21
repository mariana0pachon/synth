from wave import Wave
from midi import Midi, MidiList
from bpm import Bpm
from pygame import midi
import pyaudio
import numpy as np
import time

midi.init()
kb = midi.Input(0)

five_seconds_later = time.time() + 5
bpm_events = []
print('\nTap the "1" pad in rhythm to set the tempo')
while time.time() < five_seconds_later:
    if kb.poll():
        bpm_events.append(kb.read(1)[0])

bpm = Bpm(bpm_events).timestamps_to_bpm()
print('\nYour BPM is {}'.format(bpm))

eight_beats_later = time.time() + ((8 / bpm) / 60)
while time.time() < eight_beats_later:
    # record stuff
    pass

kb.close()
midi.quit()
