# Locating Restriction Sites
def complement(dna):
    complement = ''
    for i in dna:
        if i == 'A':
            complement += 'T'
        elif i == 'T':
            complement += 'A'
        elif i == 'C':
            complement += 'G'
        else:
            complement += 'C'
    return complement

def palindrome(val):
    dna = complement(val)
    palindrome = ''
    for i in range(len(dna) - 1, -1, -1):
        palindrome += dna[i]
    return palindrome

def locating_restrict():
    with open('data.txt', 'r') as f:
        reader = f.readline()
        while True:
            if not reader:
                break
            dna = ''
            reader = f.readline()
            while '>' not in reader and reader != '':
                dna += reader
                reader = f.readline()
            dna = dna.replace('\n', '')

    for i in range(0, len(dna)):
        for j in range(4, 13):
            if j + i > len(dna):
                break
            val = dna[i:(i+j)]
            if val == palindrome(val):
                print(i + 1, len(val))

locating_restrict()