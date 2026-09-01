from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        window = Counter(s1)
        for i in range(len(s2)):
            if window == Counter(s2[i:i + len(s1)]):
                return True
            else:
                continue
        return False



        