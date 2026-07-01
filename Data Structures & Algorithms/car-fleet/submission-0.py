class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p, s in zip(position, speed)]
        stack = []
        #Reverse sorted pairs list according to position
        for i in sorted(pairs)[::-1]: 
            stack.append((target - i[0])/i[1])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

        