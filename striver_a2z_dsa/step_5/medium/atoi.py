# https://leetcode.com/problems/string-to-integer-atoi/description/
class Solution:
    def myAtoi(s):
        s = s.strip()
        def fun(s):
            q = []
            for x in s:
                if x == "-" or x == "+":
                    if q: #[1,2,3]
                        if q[-1].isdigit(): return int("".join(q))
                        else:
                            return 0
                    else:
                        q += [x]
                elif x.isdigit():
                    q += [x]
                else:
                    return int("".join(q)) if len(q) and q[-1].isdigit() else 0
            return int("".join(q)) if len(q) and q[-1].isdigit() else 0
        k = fun(s)
        if k < -2**31: return -2**31
        elif k > 2**31 - 1: return 2**31 - 1
        else: return k
        
                
print(f"The standard way to convert string to integer: {Solution.myAtoi('4193 with words')}")
# s = "42"
# s = "   -42"
# s = "4193 with words"
# s = "+-42"