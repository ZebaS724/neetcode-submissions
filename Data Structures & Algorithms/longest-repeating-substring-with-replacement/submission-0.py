class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        res = 0
        count = [0] * 26
        
        for r in range (len(s)):
            count[ord(s[r]) - ord('A')] += 1
            max_count = max(count)
            current_rep = (r-l+1) - max_count
            
            if current_rep > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1

            res = max(res,r - l + 1)

        return res




        