
from __future__ import division
import random
import numpy
import sys
import matplotlib.pyplot as plt
from mido import Message, MidiFile, MidiTrack, MAX_PITCHWHEEL, MetaMessage, UnknownMetaMessage
def arraytomidi(fitxer):
    notes = fitxer
    outfile = MidiFile()
    track = MidiTrack()
    lll = 0
    outfile.tracks.append(track)
    wa = 0

    print(len(notes))
    ar = notes[0]
    outfile.type = int(ar[0])
    print (int(ar[0]))
    ar = notes[1]
    outfile.ticks_per_beat = int(ar[0])
    print(int(ar[0]))
    ar = notes[2]
    outfile.charset = (ar[0])
    print(outfile.charset)
    for i in range(len(notes)-1):
        i = i+1
        ar = notes[i]
        if (ar != []):
            if (isinstance(ar[0], int)==True):
                if (ar[0] == 1 and len(ar)==4):
                    track.append(Message('note_on', note=ar[2], velocity=ar[3], time=ar[4]))
                elif (ar[0] == 0 and len(ar)==4):
                    track.append(Message('note_off', note=ar[2], velocity=ar[3], time=ar[4]))
                elif (ar[0] == 1 and len(ar)==5):
                    track.append(Message('note_on', channel = ar[1], note=ar[2], velocity=ar[3], time=ar[4]))
                    lll = lll+1
                elif (ar[0] == 0 and len(ar)==5):
                    track.append(Message('note_off', channel = ar[1], note=ar[2], velocity=ar[3], time=ar[4]))
                    lll = lll+1
                elif (len(ar)==3 and ar[0]==0):
                    track.append(Message('note_off', note=ar[0], velocity=64, time=ar[1]))
                elif (len(ar)==3 and ar[0]==1):
                    track.append(Message('note_on', note=ar[0], velocity=64, time=ar[1]))

            else:
                e = ar[0]
                if (e[2] == 'end_of_track'):
                    l2 = e[3].split("=")
                    e2 = l2[1].replace('>', '')
                    track.append(MetaMessage(type='end_of_track', time=int(e2)))
                    if (i+1<len(notes)):
                        ar2 = notes[i+1]
                        ee = ar2[0]
                        if (ee[2]!='track_name'):
                            if (outfile.type != 0):
                                track = MidiTrack()
                                track.append(MetaMessage(type='track_name', name=("track"+str(wa)), time=int(e2)))
                                outfile.tracks.append(track)
                            else:
                                track.append(MetaMessage(type='track_name', name=("track" + str(wa)), time=int(e2)))
                            wa = wa + 1


                elif (e[2] == 'track_name'):
                    l2 = e[3].split("=")
                    l3 = e[(len(e)-1)].split("=")
                    e2 = l3[1].replace('>', '')
                    if (outfile.type != 0):
                        track = MidiTrack()
                        a = str(l2[1])
                        track.append(MetaMessage(type='track_name', name=a, time=int(e2)))
                        outfile.tracks.append(track)
                    else:
                        a = str(l2[1])
                        track.append(MetaMessage(type='track_name', name=a, time=int(e2)))
                    print("aaaaaaldfjasd")
                elif (e[2] == 'time_signature'):
                    l2 = e[3].split("=")
                    l3 = e[4].split("=")
                    l4 = e[5].split("=")
                    l5 = e[6].split("=")
                    l6 = e[7].split("=")
                    e2 = l6[1].replace('>', '')
                    track.append(MetaMessage(type="time_signature", numerator=int(l2[1]), denominator=int(l3[1]),
                                             clocks_per_click=int(l4[1]), notated_32nd_notes_per_beat=int(l5[1]),
                                             time=int(e2)))
                elif (e[2] == 'key_signature'):
                    l2 = e[3].split("=")
                    e1 = l2[1]
                    l3 = e[4].split("=")
                    e2 = l3[1].replace('>', '')
                    track.append(MetaMessage(type="key_signature", key=e1[1], time=int(e2)))
                elif (e[2] == 'set_tempo'):
                    l2 = e[3].split("=")
                    l3 = e[4].split("=")
                    e2 = l3[1].replace('>', '')
                    track.append(MetaMessage(type="set_tempo", tempo=int(l2[1]), time=int(e2)))
                elif (e[2] == 'instrument_name'):
                    l2 = e[3].split("=")
                    l3 = e[len(e)-1].split("=")
                    e2 = l3[1].replace('>', '')
                    track.append(MetaMessage(type="instrument_name", name = l2[1], time = int(e2)))
                elif (e[0]=='program_change'):
                    l2 = e[1].split("=")
                    l3 = e[2].split("=")
                    l4 = e[3].split("=")
                    e2 = l4[1].replace('>', '')
                    track.append(Message('program_change', channel=int(l2[1]), program=int(l3[1]), time = int(e2)))
                elif (e[0]=='control_change'):
                    l2 = e[1].split("=")
                    l3 = e[2].split("=")
                    l4 = e[3].split("=")
                    l5 = e[4].split("=")
                    e2 = l5[1].replace('>', '')
                    track.append(Message('control_change', channel=int(l2[1]), control=int(l3[1]), value = int(l4[1]), time=int(e2)))
                elif (e[0]=='sysex'):
                    l2 = e[1].split("=")
                    l3 = e[2].split("=")
                    e2 = l3[1].replace('>', '')
                    e3 = l2[1].split(',')
                    e4 = []
                    for w in e3:
                        o = w.replace('(', '')
                        o = o.replace(')', '')
                        e4.append(int(o))
                    track.append(Message(type= 'sysex', data=e4, time=int(e2)))

                elif (e[2]=='midi_port'):
                    l2 = e[3].split("=")
                    l3 = e[4].split("=")
                    e2 = l3[1].replace('>', '')
                    track.append(MetaMessage(type='midi_port', port=int(l2[1]), time=int(e2)))
                elif (e[2]=='lyrics'):
                    l2 = e[3].split("=")
                    l3 = e[len(e) - 1].split("=")
                    e2 = l3[1].replace('>', '')
                    track.append(MetaMessage(type="lyrics", text=l2[1], time=int(e2)))
                else:
                    print("CIGUEÑA")
                    print(e)



    print("si")
    print (lll)
    outfile.save('tests2/test1-1.MID')


def miditoarray():
    if __name__ == '__main__':
        w = 0
        mat = []
        arr = []
        midi_file = MidiFile('Songs/beatles-imagine.mid')
        arr.append(midi_file.type)
        mat.append(arr)
        arr = []
        arr.append(midi_file.ticks_per_beat)
        mat.append(arr)
        arr = []

        arr.append(midi_file.charset)
        mat.append(arr)
        arr = []
        print(midi_file.ticks_per_beat)
        print(midi_file.type)
        for i, track in enumerate(midi_file.tracks):
            sys.stdout.write('=== Track {}\n'.format(i))
            for message in track:

                e = (format(message).split())
                if (e[0] == 'program_change'):
                    arr.append(e)
                elif (e[0] == '<meta'):
                    arr.append(e)

                elif (e[0] == 'pitchwheel'):
                    l1 = (e[1].split('='))
                    l2 = (e[2].split('='))
                    l3 = (e[3].split('='))
                    arr.append(int(l1[1]))
                    arr.append(int(l2[1]))
                    arr.append(int(l3[1]))
                elif (e[0] == 'note_on' or e[0]== 'note_off'):

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
                elif (e[0]=='control_change'):
                    arr.append(e)
                elif(e[0]=='sysex'):
                    arr.append(e)
                else:
                    arr.append("ajuda")

                mat.append(arr)


                arr = []

                w = w + 1
    else:
        print("aveurequepasa")

    return mat
def graficador(s):
    nota = []
    temps = []
    oo = []
    onota = []
    otemps = []
    matriu = []
    meta = []
    i = 0
    e=0
    oe=0
    for c in s:
        if (len(c)!=0 and len(c)!=1 and len(c)==5):
            oo.append(c[0])
            if (c[0]==1):
                if(c[3]!=0):
                    nota.append(c[2])
                    if(temps!=[]):
                        temps.append(c[4]+temps[e])
                        e = e + 1
                    else:
                        temps.append(c[4] + 0)
                elif(temps[-1]>500):
                    break
            elif (c[0]==0):
                if (c[3] != 0):
                    onota.append(c[2])
                    if (otemps != []):
                        otemps.append(c[4] + otemps[oe])
                        oe = oe + 1
                    else:
                        otemps.append(c[4] + 0)

        elif (isinstance(c[0], int)==False and c[0]!="latin1"):
            print ("eeoo")
            oo.append(2)
            a = c[0]
            meta.append(a)
    plt.plot(temps, nota)
    plt.title('Test 1')
    plt.xlabel('Temps')
    plt.ylabel('Nota')
    plt.show()
    matriu.append(s[0])
    matriu.append(s[1])
    matriu.append(s[2])
    i = 0
    l = 0
    p = 0
    for y in oo:
        if (y==0):
            if (l!=0):
                matriu.append([y, onota[l],otemps[l]-otemps[l-1]])
            else:
                matriu.append([y, onota[l], otemps[l]])
            l = l + 1
        elif (y==1):
            if (i!=0):
                matriu.append([y, nota[i],temps[i]-temps[i-1]])
            else:
                matriu.append([y, nota[i], temps[i]])
            i = i + 1
        elif (y==2):
            matriu.append(meta[p])
            p = p + 1
    print (matriu)
    return (matriu)
arraytomidi(graficador(miditoarray()))
