#!/usr/bin/python

dna = raw_input()

rev = ""

def complement(s):
    if s=='A':
        return 'T'
    if s=='G':
        return 'C'
    if s=='C':
        return 'G'
    if s=='T':
        return 'A'

for i in range(len(dna)):
    rev = rev + complement(dna[len(dna)-1-i])

print rev
