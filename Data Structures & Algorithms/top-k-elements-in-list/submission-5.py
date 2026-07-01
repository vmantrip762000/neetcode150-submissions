class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_arr = [[] for i in range(len(nums) + 1)]
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for i in count:
            freq_arr[count[i]].append(i)

        res = []
        for i in range(len(freq_arr)-1, -1, -1):
            for j in freq_arr[i]:
                res.append(j)
                if len(res) == k:
                    return res
                
            
        