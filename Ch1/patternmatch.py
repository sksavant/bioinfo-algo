#!/usr/bin/python

pattern = raw_input()
genome = raw_input()

start_positions = []

for i in range(len(genome)-len(pattern)+1):
    if pattern==genome[i:i+len(pattern)]:
        start_positions.append(str(i))

print " ".join(start_positions)
