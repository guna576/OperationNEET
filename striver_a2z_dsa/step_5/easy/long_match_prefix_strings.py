class Solution:
    def longestCommonPrefix(s):
        ll = min([len(x) for x in s])
        ans = ""
        flag = 0
        flag1 = 0
        for i in range(ll):
            for j in range(len(s)-1):
                if s[j][i] != s[j+1][i]:
                    return s[j][:i]
                else:
                    flag += 1
            if flag == len(s)-1:
                flag1 += 1
                flag = 0
        return s[0][:flag1] if flag1 else ""
    
print(f"The longst matching prefix amoing all strings is : {Solution.longestCommonPrefix(['flower','flow','flight'])}")