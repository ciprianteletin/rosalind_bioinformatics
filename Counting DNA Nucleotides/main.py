#https://rosalind.info/problems/dna/ - Counting DNA Nucleotides
def count_dna():
    dna = input()
    a = c = g = t = 0
    for i in dna:
        if i == 'A':
            a = a + 1
        elif i == 'C':
            c = c + 1
        elif i == 'G':
            g = g + 1
        else:
            t = t + 1
    return str(a) + ' ' + str(c) + ' ' + str(g) + ' ' + str(t)

print(count_dna())
