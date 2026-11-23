class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the separator after the length
            while s[j] != "#":
                j += 1

            # Extract the length
            length = int(s[i:j])

            # Move past the separator
            start = j + 1

            # Extract the actual string
            word = s[start:start + length]
            result.append(word)

            # Move to the next encoded string
            i = start + length

        return result