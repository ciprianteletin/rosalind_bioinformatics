#Counting Point Mutations
def find_mutations():
    seq1 = input()
    seq2 = input()
    mutations = 0
    for i in range(0, len(seq1)):
        if seq1[i] != seq2[i]:
            mutations += 1
    print(mutations)

find_mutations()