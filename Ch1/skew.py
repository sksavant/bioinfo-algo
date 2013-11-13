#!/usr/bin/python

#genome = "GAGCCACCGCGATA"

genome = raw_input()

l = len(genome)

#skewlist = [0 for i in range(l+1)]

diffgc = 0

minskew = 0
#nmin = 1
minlist = [0]

for i in range(l):
    if genome[i]=='G':
        diffgc=diffgc+1
    elif genome[i]=='C':
        diffgc=diffgc-1
    if diffgc<minskew:
        #nmin=1
        minlist = [i+1]
        minskew = diffgc
    elif diffgc==minskew:
        #nmin=nmin+1
        minlist.append(i+1)
    #skewlist[i+1]=diffgc

#print " ".join(map(str,skewlist))
print " ".join(map(str,minlist))
