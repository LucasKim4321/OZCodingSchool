import sys

n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
numbers.sort()
print(numbers[0],numbers[-1])

