class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_dict = defaultdict(list)
        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            s_dict[tuple(arr)].append(s)
        return list(s_dict.values())

        