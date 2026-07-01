class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        p1 = 0
        p2 = len(height) - 1
        leftMax = height[p1]
        rightMax = height[p2]
        res = 0
        while p1 < p2:
            if leftMax <= rightMax:
                p1 += 1
                leftMax = max(leftMax, height[p1])
                res += leftMax - height[p1]
                

            else:
                p2 -=1
                rightMax = max(rightMax, height[p2])
                res += rightMax - height[p2]
                
        return res

        