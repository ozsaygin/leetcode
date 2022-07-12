class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        plain = []
        count = 0

        for ch in s: 
            if ord('a') <= ord(ch) <= ord('z') or ord('A') <= ord(ch) <= ord('Z') or ord('0') <= ord(ch) <= ord('9'):
                count = count + 1
                plain.append(ch.lower())
                
        i = count - 1
        j = 0

        while i > j:
            if plain[i] != plain[j]:
                return False
            
            i = i - 1
            j = j + 1
        
        return True
            
        
            