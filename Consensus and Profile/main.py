# Consensus and Profile
def get_max_frecv(table, index):
    max = 0
    max_key = ''
    for key in table.keys():
        if max < table[key][index]:
            max = table[key][index]
            max_key = key
    return max_key

def display_frecv(frecv):
    final_out = ''
    for key in frecv.keys():
        output = key + ': '
        for i in frecv[key]:
            output += str(i) + ' '
        final_out += output + '\n'
    return final_out

def find_max_content():
    matrix = []
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
            matrix.append(dna)
    consensus = ''
    frecv = {'A': [], 'C': [], 'G': [], 'T': []}
    for i in range(0, len(matrix[0])):
        for key in frecv.keys():
            frecv[key].append(0)
        for j in range(0, len(matrix)):
            current = matrix[j][i]
            val = frecv[current][i]
            frecv[current][i] = val + 1
        consensus += get_max_frecv(frecv, i)
    print(consensus)
    print(display_frecv(frecv))

find_max_content()
