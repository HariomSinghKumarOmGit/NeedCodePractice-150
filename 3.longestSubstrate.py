class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cSet= set()
        i = 0
        ans = 0

        for j in range(len(s)):
            while s[j] in cSet:
                cSet.remove(s[i])
                i +=1
            cSet.add(s[j])
            ans = max(ans, j-i+1)
        return ans