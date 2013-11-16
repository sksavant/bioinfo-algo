#!/usr/bin/python

pattern = raw_input()

genetic_code = {}

codon_table = open("RNA_codon_table_1.txt","r")
for codon in codon_table.readlines():
    try:
        rnaname,amino = codon.split()
    except ValueError:
        rnaname = codon.split()[0]
        amino = ""
    genetic_code[rnaname] = amino

assert(len(pattern)%3==0)

peptide = ""
for i in range(len(pattern)/3):
    peptide = peptide + genetic_code[pattern[3*i:3*i+3]]
print peptide
