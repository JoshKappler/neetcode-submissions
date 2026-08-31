from collections import defaultdict
from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 1
        longest = 0
        d = defaultdict(int)
        d[s[0]] += 1
        #most_common = Counter(s[left:right]).most_common(1)[0][1]
        while True: 
            if right >= len(s) + 1:
                return longest
            slice = s[left:right] 
            most_common = max(d.values())
            if len(slice) < most_common + k:
                if len(slice) > longest:
                    longest = len(slice)
                if right == len(s): return longest
                d[s[right]] += 1
                right += 1
            elif len(slice) > most_common + k: 
                d[s[left]] -= 1
                left += 1
            elif len(slice) == most_common + k:
                if len(slice) > longest:
                    longest = len(slice)
                if right == len(s): return longest
                d[s[right]] += 1
                right += 1
        
        return longest
        


