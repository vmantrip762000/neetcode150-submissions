class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_dict = defaultdict(list)
        for s in strs:
            word_order = [0] * 26
            for c in s:
                word_order[ord(c) - ord('a')] += 1
            s_dict[tuple(word_order)].append(s)
        return list(s_dict.values())
        