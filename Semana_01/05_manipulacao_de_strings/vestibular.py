N = input()
N = int(N)

oficial = input()
candidato = input()

total = 0

for o, c in zip(oficial, candidato):
    if o == c:
        total += 1

print(total)