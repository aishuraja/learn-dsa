# s = ["anagram"] and t = ["nagaram"]

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):   # length not equal then its not anagram 
            return False
        dict1 = {}
        for i in s:
            if i in dict1:
                dict1[i] = dict1[i] +1
            else:
                dict1.update({i:1})

        dict2 = {}
        for j in t:
            if j in dict2:
                dict2[j] = dict2[j]+1
            else:
                dict2.update({j:1})

        if dict1 != dict2:
            return False
        return True  
        

        