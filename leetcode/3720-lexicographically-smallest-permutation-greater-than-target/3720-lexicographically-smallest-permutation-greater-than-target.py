from collections import Counter
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        

    
        n = len(s)
        
        # Iterate from the longest possible prefix to the shortest
        for i in range(n - 1, -1, -1):
            prefix = target[:i]
            count_s = Counter(s)
            
            # Check if target[:i] can be formed using characters from s
            possible = True
            for ch in prefix:
                if count_s[ch] > 0:
                    count_s[ch] -= 1
                else:
                    possible = False
                    break
            
            if not possible:
                continue
            
            # Find the smallest available character strictly greater than target[i]
            for c_num in range(ord(target[i]) + 1, ord('z') + 1):
                ch = chr(c_num)
                if count_s[ch] > 0:
                    count_s[ch] -= 1
                    # Append the remaining available characters in sorted order
                    rem = sorted(count_s.elements())
                    return prefix + ch + "".join(rem)
                    
        return ""
