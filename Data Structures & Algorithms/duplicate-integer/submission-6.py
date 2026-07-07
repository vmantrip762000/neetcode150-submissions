class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set -no repeated entries
        # array repitition allowed
        # we check if length is different to return true
        return len(set(nums)) != len(nums)
        
        