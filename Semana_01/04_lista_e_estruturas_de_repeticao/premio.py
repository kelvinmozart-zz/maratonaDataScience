N = int(input())

visual = []
for i in range(N):
    A = int(input())
    visual.append(A)

total = 0
resposta = -1

for i, v in enumerate(visual):
    dia = i + 1
    total = total + v
    if total >= 1000000 and resposta == -1:
        resposta = dia

print(resposta)
