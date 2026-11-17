class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_map = defaultdict(list)

        for s in strs:
            unique_key = [0] * 26

            for c in s:
                unique_key[ord(c) - ord("a")] += 1

            strs_map[tuple(unique_key)].append(s)

        return list(strs_map.values())