#!/usr/bin/python

def complement(s):
    if s=='A':
        return 'T'
    if s=='G':
        return 'C'
    if s=='C':
        return 'G'
    if s=='T':
        return 'A'

def get_complement(dna):
    rev = ""
    for i in range(len(dna)):
        rev = rev + complement(dna[len(dna)-1-i])
    return rev


if __name__=="__main__":
    dna = raw_input()
    print get_complement(dna)

