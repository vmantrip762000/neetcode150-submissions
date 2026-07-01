class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward_arr = [1] * len(nums)
        for i in range(1, len(nums)):
            forward_arr[i] = forward_arr[i - 1] * nums[i - 1]
        
        backward_arr = [1] * len(nums)
        for i in range(len(nums) - 1, 0, -1):
            backward_arr[i - 1] = backward_arr[i] * nums[i]

        final_arr =[]
        for i in range(len(nums)):
            final_arr.append(forward_arr[i] * backward_arr[i])
        return final_arr
        