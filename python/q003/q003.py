class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bg = 0
        ed = 0
        max = ed - bg
        while ed < len(s):
            if s[ed] in s[bg:ed]:
                bg += s[bg:ed].index(s[ed]) + 1
                ed += 1
            else:
                ed += 1
                if ed - bg > max:
                    max = ed - bg
        return max
