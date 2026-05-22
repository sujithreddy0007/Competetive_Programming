import sys
input = sys.stdin.readline
import math
MOD = 10 ** 9 + 7
N = 10 ** 6
fact = [1] * (N+1)
invFact = [1] * (N+1)
 
def modPow(a,b):
    return pow(a,b,MOD)
 
for i in range(2,N+1):
    fact[i] = (i * fact[i-1]) % MOD
 
invFact[N] = modPow(fact[N],MOD-2)
for i in range(N-1,-1,-1):
    invFact[i] = (invFact[i+1] * (i+1)) % MOD
def ncr(n,r):
   
    return ((fact[n] % MOD) * (invFact[n-r] % MOD) * (invFact[r])) % MOD
for _ in range(int(input())):
    n,r = map(int,input().split())
    print(ncr(n,r))
