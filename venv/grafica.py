from __future__ import division
import random
import numpy
import sys
from mido import Message, MidiFile, MidiTrack, MAX_PITCHWHEEL, MetaMessage, UnknownMetaMessage
import matplotlib.pyplot as plt


def separador(s):
    nota = [0]
    temps = [0]
    e=0
    for c in s:
        if (len(c)!=0 and len(c)!=1 and c[0]==1):
            nota.append(c[3])
            print(c)
            temps.append(c[4]+temps[e])
            e = e + 1
    plt.plot(temps, nota)
    plt.title('Test 1')
    plt.xlabel('Temps')
    plt.ylabel('Nota')
    plt.show()
    return 0

