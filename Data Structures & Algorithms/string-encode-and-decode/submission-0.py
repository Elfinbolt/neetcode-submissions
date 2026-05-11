class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""

        for s in strs:
            enc += str(len(s)) + "#" + s

        return enc

    def decode(self, s: str) -> List[str]:
        output = []

        i = 0

        while i < len(s):

            s_len = ""

            while s[i] != "#":
                s_len += s[i]
                i += 1

            length = int(s_len)

            i += 1

            word = s[i:i + length]

            output.append(word)

            i += length

        return output