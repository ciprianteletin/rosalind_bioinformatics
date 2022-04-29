#Enumerating Gene Orders

import numpy as np
import itertools

n = 6
elemente = np.arange(1, n + 1, 1)
numar = 0

permutari = list(itertools.permutations(elemente))

print(len(permutari))

for i in permutari:
    numar += 1
    for x in range(n):
        if x < n - 1:
            print(str(i[x]), end=" ")
        else:
            print(str(i[x]))
