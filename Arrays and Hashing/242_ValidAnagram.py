# 242: Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # return Counter(s) == Counter(t)
        # return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False

        # init hashmaps
        hashS, hashT = {}, {}

        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i], 0) # value of key = 1 + existing value (default 0 if not in hashmap yet)
            #print(hashS)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)
            #print(hashT)

        # iterate through hashS
        for x in hashS:
            if hashS[x] != hashT.get(x, 0): # use .get incase the key 'x' doesn't exist in hashT, so it returns default value of 0
                return False
        
        return True