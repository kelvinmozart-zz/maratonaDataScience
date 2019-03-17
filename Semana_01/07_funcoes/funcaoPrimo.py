def eh_primo(x):
    count = 0

    if x <= 1:
        return False

    for i in range(1, (x//2)+1):
        if x % i == 0:
            count += 1

    if (count == 1):
        return True
    else:
        return False


x = int(input())

if eh_primo(x):
    print('S')
else:
    print('N')