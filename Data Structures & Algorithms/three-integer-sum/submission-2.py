class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i, j = 0, len(nums) - 1
        op_list = []
        for i in range(0, len(nums) - 2):
            for j in range(i + 2, len(nums)):
                for k in range(i + 1, j):
                    if nums[i] + nums[j] + nums[k] == 0:
                        if sorted([nums[i], nums[j], nums[k]]) not in op_list:
                            op_list.append(sorted([nums[i], nums[j], nums[k]]))
        return op_list
        