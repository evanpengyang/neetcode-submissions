class Solution:

    def encode(self, strs: List[str]) -> str:
        megastring = ""

        for s in strs:
            length = len(s)
            megastring += str(length) + "#" + s

        return megastring

        
    def decode(self, s: str) -> List[str]:
        strs = []
        numchars = ""
        i = 0

        while i < len(s):
            if s[i] == "#":
                strs.append(s[i + 1:i + 1 + int(numchars)])
                i += int(numchars) + 1
                numchars = ""
            else:
                numchars += s[i]
                i += 1

        return strs