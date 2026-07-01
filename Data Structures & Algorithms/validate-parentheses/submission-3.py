class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0: return False
        my_stack = []
        s_dict = {'(':')', '[':']', '{':'}'}
        for i in s:
            if i in s_dict:
                my_stack.append(i)
            else:
                if len(my_stack) > 0 and s_dict[my_stack.pop()] == i:
                    continue
                else:
                    return False
                
        return len(my_stack) == 0




        