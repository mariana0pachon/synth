'''
    BPM class
    Calculate BPM based on finger tapping timing
'''
from midi import MidiList
import numpy as np

class Bpm:

    def __init__(self, events):
        self.events = MidiList(events).midi_events

    def timestamps_to_bpm(self):
        tapping_times = []

        reference_ev = self.events[0]
        for ev in self.events:
            if ev.status == reference_ev.status and ev.data1 == reference_ev.data1:
                tapping_times.append(ev.timestamp)

        gaps = [tapping_times[i+1]-tapping_times[i] for i in range(len(tapping_times)-1)]

        return int(60 / (np.mean(gaps)/1000))
