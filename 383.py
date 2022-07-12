import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ransom_note_chars = collections.Counter(ransomNote)
        magazine_chars = collections.Counter(magazine)
        
        for k, v in ransom_note_chars.items():
            if v > magazine_chars[k]:
                return False
            
        return True
        