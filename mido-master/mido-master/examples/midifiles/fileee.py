
from __future__ import division
import random
import sys
from mido import Message, MidiFile, MidiTrack, MAX_PITCHWHEEL

notes = input()

outfile = MidiFile()

track = MidiTrack()
outfile.tracks.append(track)

track.append(Message('program_change', program=12))

delta = 300
ticks_per_expr = int(sys.argv[1]) if len(sys.argv) > 1 else 20
for i in range(len(notes)):
    ar = notes[i]
    if (ar != []):
        if (ar[0] == 1):
            track.append(Message('note_on', note=ar[2], velocity=ar[3], time=ar[4]))
        elif (ar[0] == 0):
            track.append(Message('note_off', note=ar[2], velocity=ar[3], time=ar[4]))
        elif (ar[0]== "Track"):
            i = len(notes)
outfile.save('test4.mid')