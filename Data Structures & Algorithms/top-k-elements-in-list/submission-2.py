class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1
        print(dic)
        res = dict(sorted(dic.items(), key = lambda x: x[1], reverse=True))
        print(res)
        return list(res.keys())[:k]