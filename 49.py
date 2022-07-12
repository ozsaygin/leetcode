class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = { }
        output = [ ] 
        for str in strs: 
            sorted_str = sorted(list(str))
            sorted_str = "".join(sorted_str)

            if sorted_str not in anagrams: 
                anagrams[sorted_str] = [ ]

            anagrams[sorted_str].append(str)

        for k, v in anagrams.items(): 
            output.append(v)

        return output
        