from instrument import Instrument
from wave import Wave
from scipy.io import wavfile
from subprocess import call
import sys

while True:
    inst = input('Enter instrument (pure, oboe, etc)\n')
    wave = input('Enter wave shape (sine, triangle, saw, square)\n')
    notes = input('Enter sequence of Notes\n')
    seq = Instrument(notes.strip().split(' ')).generate_wave_list()

    i = 0
    for s in seq:
        new_file = 'ex2_{}.wav'.format(i)
        wavfile.write(new_file, Wave.rate, s.shape)

        if 'darwin' in sys.platform:
            call(['afplay', new_file])

        elif 'linux' in sys.platform:
            call(['aplay', new_file])
        i = i + 1
