
def fatorial(N):
    fat = 1
    i = 2
    while i <= N:
        fat = fat*i
        i = i + 1

    return fat

N = int(input())
print(fatorial(N))