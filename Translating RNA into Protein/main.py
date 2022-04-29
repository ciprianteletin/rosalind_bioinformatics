#Translating RNA into Protein
def read_table(table):
    with open('table.txt', 'r') as f:
        line = f.readline()
        while line != '':
            key, value = line.split(' ')
            table[key] = value.replace('\n', '')
            line = f.readline()

def rna_to_protein():
    table = dict()
    read_table(table)
    dna = input()
    rna = ''
    for i in range(0, len(dna), 3):
        val = dna[i:(i+3)]
        table_val = table[val]
        if table_val == 'Stop':
            break
        rna += table_val
    return rna

print(rna_to_protein())
