table = dict()
def read_table():
    with open('table.txt', 'r') as f:
        line = f.readline()
        while line != '':
            key, val = line.split(' ')
            table[key] = val
            line = f.readline()

def compute():
    read_table()
    sum = 0
    protein = input()
    for i in protein:
        sum += float(table[i])
    return sum

print(compute())