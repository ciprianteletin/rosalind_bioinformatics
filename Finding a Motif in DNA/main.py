#Finding a Motif in DNA
#Brute force approach

def find_motifs():
    dna = input()
    motif = input()
    list = []
    for i in range(0, len(dna)-len(motif)+1):
        check = dna[i:(i + len(motif))]
        if check == motif:
            list.append(i+1)
    out = ''
    for i in list:
        out += str(i) + ' '
    print(out)

find_motifs()