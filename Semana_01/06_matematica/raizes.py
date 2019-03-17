import math
N = int(input())
raiz = input().split()

for i in range(N):
    raiz[i] = float(raiz[i])
    print("{0:.4f}".format(math.sqrt(raiz[i])))
