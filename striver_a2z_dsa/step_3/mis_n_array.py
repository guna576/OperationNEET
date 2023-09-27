l = [1,2,3,5,6,7,8,9]
print(((l[-1]*(l[-1]+1))//2))
print(f"The missing number in {l} is {((l[-1]*(l[-1]+1))//2) - sum(l)}")

ans = 0
for i in range(len(l)-1):
    if l[i] + 1 != l[i+1]:
        print(l[i]+1)
        break

xor1,xor2 = 0,0 

for i in range(len(l)):
    xor1 ^= l[i]
    xor2 ^= (i+1)

print(xor1^xor2^l[-1])  # We need to xor the last element aka no. of elements 

#Same TC O(N)