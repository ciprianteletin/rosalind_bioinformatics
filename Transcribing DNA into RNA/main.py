#https://rosalind.info/problems/rna/ - Transcribing DNA into RNA
def transform(dna):
    rna = ''
    for i in dna:
        if i == 'T':
            rna += 'U'
        else:
            rna += i
    return rna

dna = input()
print(transform(dna))