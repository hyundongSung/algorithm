from sys import stdin

a, b, c = map(int, stdin.readline().split(' '))

print(f'{(a + b) % c}')
print(f'{((a % c) + (b % c)) % c}')
print(f'{(a*b) % c}')
print(f'{((a % c) * (b % c)) % c}')
