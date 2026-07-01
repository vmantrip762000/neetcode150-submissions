class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "$" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        s_list = []
        i = 0
        while i <= len(s) - 1:
            j = i
            while s[j] != "$":
                j+=1
            length = int(s[i:j])
            new_str = s[j + 1:j + 1 + length]
            s_list.append(new_str) 
            i = j + 1 + length
        return s_list 
