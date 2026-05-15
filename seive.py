import sys
input = sys.stdin.readline

n = int(input())

sieve = [True] * (n + 1)
sieve[0] = sieve[1] = False

i = 2
while i * i <= n:
    if sieve[i]:
        for j in range(i * i, n + 1, i):
            sieve[j] = False
    i += 1

primes = []


for i in range(2, n + 1):
    if sieve[i]:
        primes.append(i)

print(primes)