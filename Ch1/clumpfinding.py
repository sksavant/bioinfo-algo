#!/usr/bin/python

genome = raw_input()
mykmers = []

tlen = len(genome)
k,l,t = map(int, raw_input().split())

def findkmers(text,t,k):
    kdict = {}

# Create a dictionary of k-mers incrementing by 1 everytime you get one
# Store the max no. of times a k-mer has occured
# When all done, go through the dict to see all k-mers having max number

    maxval = 0

    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        #print pattern
        try:
            kdict[pattern] = kdict[pattern] + 1
        except KeyError:
            kdict[pattern] = 1
        if maxval < kdict[pattern]:
            maxval = kdict[pattern]
    for k in kdict.keys():
        if kdict[k] >=t and k not in mykmers:
            print k,
            mykmers.append(k)


for genindex in range(tlen-l+1):
    partgen = genome[genindex:genindex+l]
    findkmers(partgen,t,k)

