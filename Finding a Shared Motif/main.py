#Finding a Shared Motif
def read_file():
    list = []
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
            list.append(dna)
    return list

def is_motif(list, motif):
    for i in list:
        if motif not in i:
            return False
    return True

def shared_motif():
    list = read_file()
    # Brute force way
    if len(list) == 0:
        return ''
    if len(list) == 1:
        return list[0]
    dna = list[0]
    motif = ''
    for i in range(0, len(dna)):
        for j in range(i + 1, len(dna)):
            possible_motif = dna[i:j]
            if is_motif(list, possible_motif) and len(possible_motif) > len(motif):
                motif = possible_motif
    return motif

print(shared_motif())
