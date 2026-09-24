class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(char.lower() for char in s if char.isalnum())
        a=len(s)-1
        b=""
        
        while a>=0 :
            
            b+=s[a]
            a-=1
        if b==s:
            return True
        else:
            return False