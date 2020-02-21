from wave import Wave
from midi import Midi, MidiList
from bpm import Bpm
from pygame import midi
import pyaudio
import numpy as np
import time

midi.init()
kb = midi.Input(0)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=Wave.rate,
                output=True)

stream_flags = [False] * 128
#streams = [stream] * 128
waves = [None] * 128

print('\nPlay notes on the MIDI controller\n')
while True:
    if kb.poll():
        message = Midi(kb.read(1)[0])
        note = message.data1

        if message.status == 128: # release event
            stream_flags[note] = False
            waves[note] = None

        if message.status == 144: # press event
            stream_flags[note] = True
            waves[note] = message.generate_wave()

    note_addition = []
    note_presence = None
    for i in range(128):
        if stream_flags[i]:
            note_addition.append(waves[i])
            note_presence = i

    if note_presence:
        addition = waves[note_presence].add_waves(note_addition)
        stream.write(waves[note_presence].vol * waves[note_presence].shape)


kb.close()
midi.quit()

stream.stop_stream()
stream.close()
p.terminate()
