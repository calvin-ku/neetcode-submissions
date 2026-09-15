class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Pack each string as: [length] + "#" + [string]
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # Move j forward until it finds the '#' delimiter
            while s[j] != "#":
                j += 1
            
            # The number is everything between i and j
            length = int(s[i:j])
            
            # The actual string starts right after '#' and goes for 'length' characters
            start = j + 1
            end = j + 1 + length
            res.append(s[start:end])
            
            # The Jump: Move i to the exact start of the next chunk
            i = end
            
        return res