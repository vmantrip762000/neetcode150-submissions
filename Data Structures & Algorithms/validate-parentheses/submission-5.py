class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0: return False
        s_dict = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in s:
            if i in s_dict:
                stack.append(i)
            elif stack and i == s_dict[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack) == 0




        