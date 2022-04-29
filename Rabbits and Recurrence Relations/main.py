#Rabbits and Recurrence Relations
def rabbit_pairs(n, k):
    if n == 1:
        return 1
    elif n == 2:
        return k
    prev = n - 1
    prev2 = n - 2
    one_gen = rabbit_pairs(prev, k)
    two_gen = rabbit_pairs(prev2, k)
    if n <= 4:
        return (one_gen + two_gen)
    return (one_gen + (two_gen * k))



n = int(input())
k = int(input())
print(rabbit_pairs(n, k))