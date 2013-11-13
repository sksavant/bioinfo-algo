#!/usr/bin/python

pattern = raw_input()
text = raw_input()
d = int(raw_input())

approxmatchlist = []

for i in range(0,len(text)-len(pattern)+1):
    nmismatch = 0
    for j in range(len(pattern)):
        if text[i+j] is not pattern[j]:
            nmismatch=nmismatch+1
    if nmismatch<=d:
        approxmatchlist.append(i)

print " ".join(map(str, approxmatchlist))
