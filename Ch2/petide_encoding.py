#!/usr/bin/python

import rna_to_amino
import revcomp

def find_possible_encoders_helper(dna_text, peptide):
    text = rna_to_amino.transcribe_dna(dna_text)
    gc = rna_to_amino.get_genetic_code()
    sublen = 3*len(peptide)
    substrings = []
    for i in range(len(text)-sublen+1):
        subs = text[i:i+sublen]
        if rna_to_amino.translate_rna(subs)==peptide:
            substrings.append(dna_text[i:i+sublen])
    print "Done with one dna seq"
    return substrings

def find_possible_encoders(text, peptide):
    return find_possible_encoders_helper(text,peptide)+map(revcomp.get_complement,find_possible_encoders_helper(revcomp.get_complement(text),peptide))

if __name__=="__main__":
    bacteria = open("B_brevis.txt","r")
    b = "".join(bacteria.read().split('\n'))
    peptide = "VKLFPWFNQY"
    #print b
    print "\n".join(find_possible_encoders(b,peptide)),
    '''
    text = raw_input()
    peptide = raw_input()
    print "\n".join(find_possible_encoders(text,peptide)),
    '''
