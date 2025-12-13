class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0]* 26 # this gives 26 zeros form a ...z
            for c in s:
                count[ord(c) - ord("a")] +=1  # this calculates the list order with respect to a liek the next letter is how mush ahed of z
            res[tuple(count)].append(s)
        return list(res.values())