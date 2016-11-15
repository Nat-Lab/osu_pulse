#!/usr/bin/env python3
import wave
import sys

BITRATE = 44100
prev = '0:0'

if len(sys.argv) < 2: 
	print('usage: ' + sys.argv[0] + ' <in_file> <out_file>')
	exit(1)


def get_audio(duration, level): return bytearray([int(127+(level)/2)]*int(BITRATE/1000*duration))

with wave.open(sys.argv[2],"w") as w:
	w.setnchannels(1)
	w.setsampwidth(1)
	w.setframerate(BITRATE)
	with open(sys.argv[1]) as f:
		for line in f:
			prev_time = int(prev.split(':')[0])
			prev_vol  = int(prev.split(':')[1])
			this_time = int(line.split(':')[0])
			this_vol  = int(line.split(':')[1])
			w.writeframes(get_audio(this_time - prev_time, prev_vol))
			prev = line
