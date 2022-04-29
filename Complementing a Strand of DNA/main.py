# Complementing a Strand of DNA
def reverseComplementary(dna):
    reverseDna = reversed(dna)
    complement = ''
    for i in reverseDna:
        if i == 'A':
            complement += 'T'
        elif i == 'T':
            complement += 'A'
        elif i == 'C':
            complement += 'G'
        else:
            complement += 'C'
    return complement

dna = input()
print(reverseComplementary(dna))