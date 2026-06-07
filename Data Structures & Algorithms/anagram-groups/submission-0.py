class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            print(sorted(s))
            # sorted(s) return a list of letters
            sorted_s = "".join(sorted(s))
            res[sorted_s].append(s)
        return list(res.values())
