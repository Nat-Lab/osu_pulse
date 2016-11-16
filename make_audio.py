#!/usr/bin/env python3
import wave
import sys
import math

BITRATE = 44100
FREQ = 100
prev = '0:0'

if len(sys.argv) < 4: 
	print('usage: ' + sys.argv[0] + ' <in_file> <out_file> <sine|digital>')
	exit(1)

def frame_time(n): 
	if n == 0: return n
	return BITRATE/n
def get_audio(duration, level): return bytearray([int(127+(level)/2)]*int(BITRATE/1000*duration))
def get_audio_vary(duration, level):
	result = []
	frames_count = int(BITRATE/1000*duration)
	for i in range(0, frames_count):
		result.append(int((math.sin(frame_time(i)%FREQ)*127+128)*(level/255)))
	return bytearray(result)


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
			if sys.argv[3] == 'digital': w.writeframes(get_audio(this_time - prev_time, prev_vol))
			else: w.writeframes(get_audio_vary(this_time - prev_time, prev_vol))
			prev = line
