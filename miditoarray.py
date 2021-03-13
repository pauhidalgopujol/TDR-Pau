#!/usr/bin/env python
"""
Open a MIDI file and print every message in every track.

Support for MIDI files is still experimental.
"""
import sys
import numpy
from mido import MidiFile

if __name__ == '__main__':
    w = 0
    mat = []
    arr = []
    midi_file = MidiFile('BRAND1.mid')
    print (midi_file.tracks)

    for i, track in enumerate(midi_file.tracks):
        sys.stdout.write('=== Track {}\n'.format(i))
        for message in track:
            sys.stdout.write('  {!r}\n'.format(message))
            e = (format(message).split())
            print (e)
            if (e[0]=='program_change'):
                arr.append(e)

            elif (e[0] == '<meta'):
                print ("data")
                arr.append(e)
            elif (e[0] == 'pitchwheel'):
                l1 = (e[1].split('='))
                l2 = (e[2].split('='))
                l3 = (e[3].split('='))
                arr.append(int(l1[1]))
                arr.append(int(l2[1]))
                arr.append(int(l3[1]))
            else:
                print (e[0])
                if (e[0]=="note_on"):
                    arr.append(1)
                else:
                    arr.append(0)
                l1 = (e[1].split('='))
                l2 = (e[2].split('='))
                l3 = (e[3].split('='))
                l4 = (e[4].split('='))
                arr.append(int(l1[1]))
                arr.append(int(l2[1]))
                arr.append(int(l3[1]))
                arr.append(int(l4[1]))

            mat.append(arr)

            print (arr)
            arr = []
            print (mat[w])
            w = w + 1
print (mat)
