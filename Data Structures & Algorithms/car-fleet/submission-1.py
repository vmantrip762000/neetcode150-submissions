class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        my_stack = []
        for p, s in sorted(pair)[::-1]:
            my_stack.append((target - p)/s)
            if len(my_stack) > 1 and my_stack[-1] <= my_stack[-2]:
                my_stack.pop()
        return len(my_stack)
        