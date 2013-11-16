#!/usr/bin/python

def get_mass_table():
    masses = {}
    massfile = open("integer_mass_table.txt","r")
    for line in massfile.readlines():
        amino,mass = line.split()
        mass = int(mass)
        masses[amino] = mass
    return masses

def cyclo_spectrum(peptide):
    mass_table = get_mass_table()
    mass_array = []
    spectrum = []
    for amino in peptide:
        mass_array.append(mass_table[amino])
    spectrum.append(0)
    spectrum.append(sum(mass_array))
    n = len(mass_array)
    for i in range(n):
        mass = 0
        for j in range(n-1):
            mass = mass + mass_array[(i+j)%n]
            spectrum.append(mass)
    return sorted(spectrum)

def no_of_subpeptides(peptide_len):
    return peptide_len*(peptide_len-1)

if __name__=="__main__":
    #pl = int(raw_input())
    #print no_of_subpeptides(pl)
    pep = raw_input()
    print " ".join(map(str,cyclo_spectrum(pep)))
