
from __future__ import division
import random
import numpy
import sys
from mido import Message, MidiFile, MidiTrack, MAX_PITCHWHEEL
def arraytomidi(fitxer):
    notes = fitxer
    outfile = MidiFile()
    track = MidiTrack()
    outfile.tracks.append(track)
    track.append(Message('program_change', program=12))
    delta = 300
    ticks_per_expr = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    for i in range(len(notes)):
        ar = notes[i]
        print (ar)
        if (ar != []):
            if (ar[0] == 1 and len(ar)==4):
                track.append(Message('note_on', note=ar[2], velocity=ar[3], time=ar[4]))
            elif (ar[0] == 0 and len(ar)==4):
                track.append(Message('note_off', note=ar[2], velocity=ar[3], time=ar[4]))
            else:
                track.append(Message(ar))

    outfile.save('test6.mid')


def miditoarray():
    if __name__ == '__main__':
        w = 0
        mat = []
        arr = []
        midi_file = MidiFile('ITALCONC.MID')

        for i, track in enumerate(midi_file.tracks):
            sys.stdout.write('=== Track {}\n'.format(i))
            for message in track:
                sys.stdout.write('  {!r}\n'.format(message))
                e = (format(message).split())
                print(e)
                if (e[0] == 'program_change'):
                    p = e[1]
                    print("inici " + p)
                    arr.append("start")
                elif (e[0] == '<meta'):
                    print("data")
                    arr.append("metadata")
                elif (e[0] == 'pitchwheel'):
                    l1 = (e[1].split('='))
                    l2 = (e[2].split('='))
                    l3 = (e[3].split('='))
                    arr.append(int(l1[1]))
                    arr.append(int(l2[1]))
                    arr.append(int(l3[1]))
                else:
                    print(e[0])
                    if (e[0] == "note_on"):
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

                print(arr)
                arr = []
                print(mat[w])
                w = w + 1
    return mat
arraytomidi(miditoarray())