class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        
        numSet = set(nums)
        for n in nums:
            length = 0
            if n - 1 not in numSet:
                while n + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

        