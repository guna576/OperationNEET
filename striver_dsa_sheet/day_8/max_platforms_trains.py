# You got this in Amazon TR1 Q1
from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def calculateMinPatforms(l, m, n):
    l.sort()
    m.sort()
    ans = 1
    cnt = 1
    i,j = 1,0
    while i < n and j < n:
        if l[i] <= m[j]:  # You are doing mistake here, if the rep and arr equal still the platform is needed
            cnt += 1
            i += 1
        else:
            cnt -= 1
            j += 1
        ans = max(ans,cnt)
    return ans

# O(NlogN) and O(N)

# Taking the input.
def takeInput():
    n = int(stdin.readline().strip())
    at = list(map(int, stdin.readline().strip().split(" ")))
    dt = list(map(int, stdin.readline().strip().split(" ")))

    return at, dt, n

# Main.
T = int(input())
while (T > 0):
    T -= 1
    at, dt, n = takeInput()
    minNumOfPlatforms = calculateMinPatforms(at, dt, n)
    print(minNumOfPlatforms)


##############################################################################

# 2
# 6
# 900 940 950 1100 1500 1800
# 910 1200 1120 1130 1900 2000
# 1
# 2    
# 900 940    
# 910 1200
