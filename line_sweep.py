
# Used for intervals (to maintain current active intervals)


for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    sweep = []
    for i in range(n):
        sweep.append((A[i],-1))
        sweep.append((B[i],+1))
        
    sweep.sort(key = lambda x : (x[0],-x[1]))
    curr,maxi = 0,0
    for time,status in sweep:
        if status == -1:
            curr += 1
        else:
            curr -= 1
        maxi = max(maxi,curr)
    print(maxi)