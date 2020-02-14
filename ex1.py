from instrument import Instrument
from wave import Wave
from scipy.io import wavfile
from subprocess import call
from sys import platform

inst = Instrument(['c', 'e', 'f', '[c,e,f]'], inst_name='organ').generate_wave_list()

i = 0
for elt in inst:
    new_file = 'ex1_{}.wav'.format(i)
    wavfile.write(new_file, Wave.rate, elt.shape)

    if 'darwin' in platform:
        call(['afplay', new_file])

    elif 'linux' in platform:
        call(['aplay', new_file])
    i = i + 1 
