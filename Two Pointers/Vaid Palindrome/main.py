class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        string = ''.join(filter(str.isalnum, s))
        string = string.lower()
        rev = string[::-1]
        
        if string == rev:
            return True
        
        return False