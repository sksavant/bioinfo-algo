#!/usr/bin/python

genome = raw_input()
print "Read the genome into  string"
mykmers = []

tlen = len(genome)
k,l,t = map(int, raw_input().split())

def findkmers(genind, t,k):
    # tect = partgen = genome[genindex:genindex+l]
    kdict = {}

# Create a dictionary of k-mers incrementing by 1 everytime you get one
# Store the max no. of times a k-mer has occured
# When all done, go through the dict to see all k-mers having max number

    maxval = 0

    for i in range(len(genome[genindex:genindex+l])-k+1):
        pattern = genome[genindex+i:genindex+l+i+k]
        #print pattern
        try:
            kdict[pattern] = kdict[pattern] + 1
        except KeyError:
            kdict[pattern] = 1
        if maxval < kdict[pattern]:
            maxval = kdict[pattern]
    for k in kdict.keys():
        if kdict[k] >=t and k not in mykmers:
            #print k,
            mykmers.append(k)
            print len(mykmers)

for genindex in range(tlen-l+1):
    findkmers(genindex,t,k)
    print genindex
print len(mykmers)

