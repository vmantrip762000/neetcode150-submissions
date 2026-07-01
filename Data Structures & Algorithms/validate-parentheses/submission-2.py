class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {'{':'}', '[':']', '(':')'}
        stack = []
        for i in s:
            if i in my_dict :
                stack.append(i)
            else:
                if len(stack) != 0:
                    pop_val = stack.pop()
                    if my_dict[pop_val] == i:
                        continue
                    else:
                        return False
                else:
                    return False

            
        return len(stack) == 0


        