class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #k most frequent elements => frequency array in bucket sort
        #construct array arrays
        freq_arr = [[] for i in range(len(nums) + 1)]
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # populate frequency array using the count dictionary
        for i in count:
            freq_arr[count[i]].append(i)

        # parse frequncy array in reverse order till len(res) == k
        res = []
        for i in range(len(freq_arr)-1, -1, -1):
            for j in freq_arr[i]:
                res.append(j)
                if len(res) == k:
                    return res
                

        