#!/usr/bin/python

#genome = "GAGCCACCGCGATA"

genome = raw_input()

l = len(genome)

skewlist = [0 for i in range(l+1)]

diffgc = 0

minskews = [0]

for i in range(l):
    if genome[i]=='G':
        diffgc=diffgc+1
    elif genome[i]=='C':
        diffgc=diffgc-1
    if 
    skewlist[i+1]=diffgc

print " ".join(map(str,skewlist))
