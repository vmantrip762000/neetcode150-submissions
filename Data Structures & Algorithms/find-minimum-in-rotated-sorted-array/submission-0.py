class Solution:
    def findMin(self, nums: List[int]) -> int:
        p1 = 0
        p2 = len(nums) - 1
        res = nums[0]
        while p1 <= p2:
            if nums[p1] < nums[p2]:
                res = min(res, nums[p1])
                break
            mid = p1 + (p2 - p1)//2
            res = min(res, nums[mid])
            if nums[mid] >= nums[p1]:
                p1 = mid + 1
            else:
                p2 = mid - 1
        return res

        