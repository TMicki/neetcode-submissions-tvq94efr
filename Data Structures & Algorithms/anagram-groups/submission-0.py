class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in strs:
            sortedI = ''.join(sorted(i))
            res[sortedI].append(i)
        return list(res.values())