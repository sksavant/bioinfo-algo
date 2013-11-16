#!/usr/bin/python

import rna_to_amino

genetic_code = rna_to_amino.get_genetic_code()

def find_num_possible(amino):
    assert(len(amino)==1)
    n = 0
    for k in genetic_code.keys():
        if genetic_code[k]==amino:
            n = n+1
    return n

def find_possible_dna_num(amino_seq):
    total_num = 1
    for amino in amino_seq:
        total_num = total_num*find_num_possible(amino)
    return total_num

if __name__=="__main__":
    amino_seq = raw_input()
    # VKLFPEFNQY
    print find_possible_dna_num(amino_seq)
