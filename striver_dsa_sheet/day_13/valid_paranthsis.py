class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for x in s:
            if not st: st += [x]
            elif x == ")" and st[-1] == "(": st.pop()
            elif x == "]" and st[-1] == "[": st.pop()
            elif x == "}" and st[-1] == "{": st.pop()
            else: st += [x]
        return len(st) == 0
    
# You can write better ra Falthu Doctor