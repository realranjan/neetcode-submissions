class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        b={}
        c={}

        for i in s:
            if i not in b:
                b[i]=1
            else:
                b[i]+=1

        for j in t:
            if j not in c:
                c[j]=1
            else:
                c[j]+=1

        if b==c:
            return True
        else:
            return False


        