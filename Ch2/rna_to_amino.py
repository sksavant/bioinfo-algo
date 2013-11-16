#!/usr/bin/python

def get_genetic_code():
    genetic_code = {}

    codon_table = open("RNA_codon_table_1.txt","r")
    for codon in codon_table.readlines():
        try:
            rnaname,amino = codon.split()
        except ValueError:
            rnaname = codon.split()[0]
            amino = ""
        genetic_code[rnaname] = amino
    return genetic_code

genetic_code = get_genetic_code()

def transcribe_dna(dna):
    rna = ""
    for gene in dna:
        if gene=='T':
            gene = 'U'
        rna=rna+gene
    return rna

def translate_rna(pattern):
    assert(len(pattern)%3==0)

    peptide = ""
    for i in range(len(pattern)/3):
        peptide = peptide + genetic_code[pattern[3*i:3*i+3]]
    return peptide

if __name__=="__main__":
    pattern = raw_input()
    print translate_rna(pattern)
