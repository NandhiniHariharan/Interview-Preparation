from typing import List
class ValidAnagrams:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS,countT={},{}
        for i in range(len(s)):
            countS[s[i]]=1+countS.get(s[i],0)
            countT[t[i]]=1+countT.get(t[i],0)
        return countS==countT
s=input("Enter First String:")
t=input("Enter second String:")
obj= ValidAnagrams()
print(obj.isAnagram(s,t))