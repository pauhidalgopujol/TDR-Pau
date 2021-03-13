
from __future__ import division
import random
import sys
from mido import Message, MidiFile, MidiTrack, MAX_PITCHWHEEL

notes = [64, 64+7, 64+12]

outfile = MidiFile()

track = MidiTrack()
outfile.tracks.append(track)

track.append(Message('program_change', program=12))

delta = 300
ticks_per_expr = int(sys.argv[1]) if len(sys.argv) > 1 else 20
for i in range(4):
    note = random.choice(notes)
    track.append(Message('note_on', note=note, velocity=100, time=delta))

    track.append(Message('note_off', note=note, velocity=100, time=0))

outfile.save('test.mid')
