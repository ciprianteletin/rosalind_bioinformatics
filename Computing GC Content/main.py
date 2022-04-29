# Computing GC Content
def find_max_content():
    storage = dict()
    with open('data.txt', 'r') as f:
        reader = f.readline()
        while True:
            key = reader
            if not key:
                break
            dna = ''
            reader = f.readline()
            while '>' not in reader and reader != '':
                dna += reader
                reader = f.readline()
            key = key.replace('>', '').replace('\n', '')
            dna = dna.replace('\n', '')
            cg = 0
            for i in dna:
                if i == 'C' or i == 'G':
                    cg += 1
            storage[key] = (cg * 100)/len(dna)
    max = 0
    maxkey = ''
    for k in storage.keys():
        val = storage.get(k)
        if val > max:
            maxkey = k
            max = val
    print(maxkey)
    print(max)

find_max_content()