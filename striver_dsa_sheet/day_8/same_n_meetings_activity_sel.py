def fun(n,l,m):
    z = [[l[i],m[i],i+1] for i in range(n)]
    z.sort(key = lambda x:(x[1],x[0]))
    ll = z[0][1]
    ans = [z[0][2]]

    for i in range(1,n):
        if ll <= z[i][0]:
            ans += [z[i][2]]
            ll = z[i][1]
    return ans


print(fun(6,[1,3,0,5,8,5], [2,4,5,7,9,9]))