'''
    Wave class
'''
import numpy as np
from scipy import signal

class Wave:

    rate = 44100 # sampling rate, standard is 44.1 kHz (44100 samples per sec)

    def __init__(self, freq, dur=0.2, vol=0.5, shape='sine'):
        self.freq = freq
        self.dur = dur
        self.vol = vol
        self.__t = np.arange(Wave.rate*dur)
        self.__build_shape(shape)

    def __build_shape(self, shape_string):
        if shape_string == 'triangle':
            return self.__triangle()
        elif shape_string == 'square':
            return self.__square()
        elif shape_string == 'saw':
            return self.__saw()
        else:
            return self.__sine()

    def __sine(self):
        shape = (np.sin(2 * np.pi * self.__t * self.freq / Wave.rate)).astype(np.float32)
        self.shape = shape
        return self

    def __square(self):
        shape = (signal.square(2 * np.pi * self.__t * self.freq / Wave.rate)).astype(np.float32)
        self.shape = shape
        return self

    def __saw(self):
        shape = (signal.sawtooth(2 * np.pi * self.__t * self.freq / Wave.rate)).astype(np.float32)
        self.shape = shape
        return self

    def __triangle(self):
        shape = (signal.sawtooth(2 * np.pi * self.__t * self.freq / Wave.rate, 0.5)).astype(np.float32)
        self.shape = shape
        return self

    def add_waves(self, wave_list, wts=None):
        self.freq = np.mean([w.freq for w in wave_list])
        self.dur = np.mean([w.dur for w in wave_list])
        self.vol = np.mean([w.vol for w in wave_list])
        self.shape = np.average([w.shape for w in wave_list], axis=0,
                weights=wts)
        return self
