class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for s in strs:
            new_str += str(len(s)) + "$" + s
        return new_str
        
    def decode(self, s: str) -> List[str]:
        s_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            length = int(s[i:j])
            word = s[j + 1:j + 1 + length]
            s_list.append(word)
            i = j + 1 + length              
        
        return s_list


        
