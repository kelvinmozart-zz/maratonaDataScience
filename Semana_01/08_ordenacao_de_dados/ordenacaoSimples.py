turns = int(input())
numbers = input().split()

for i in range(turns):
    numbers[i] = int(numbers[i])

numbers.sort()

for i in range(turns):
    print(numbers[i], end=" ")