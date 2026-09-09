class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            # Create an array of 26 zeros to represent the letters a-z
            count = [0] * 26 
            
            # Count the frequency of each character in the string
            for c in s:
                count[ord(c) - ord('a')] += 1
                
            # Convert the list to a tuple so it can be used as a dictionary key
            res[tuple(count)].append(s)
            
        return list(res.values())
       
            