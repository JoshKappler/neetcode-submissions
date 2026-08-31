class Solution:
    def isValid(self, s: str) -> bool:
        mp = {"(":")", "{":"}", "[":"]"} 
        opener = "([{"
        closer = ")]}"
        stk = []
        for char in s:
            if char in closer: 
                if len(stk) == 0:
                    return False
                if mp[stk.pop()] != char: 
                    return False
            else:
                stk.append(char) 
        return len(stk) == 0

            


        
        