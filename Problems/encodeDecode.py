class Solution:

    def encode(self, strs: List[str]) -> str:
        # convert the original list to single string 
        #   "4#neet4#code4#love3#you"
        encoded_string = []
        for i in strs:
            encoded_string.append(str(len(i)) + '#' + i)
        return ''.join(encoded_string)
    
    def decode(self, s: str) -> List[str]:

        # convert single string to original list 
        #       ["neet","code","love","you"]
        #       s =  "4#neet4#code4#love3#you"

        decoded_string = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!= '#':
                j+=1
            n = int(s[i:j]) # length
            j+=1
            decoded_string.append(s[j: j+n])
            i = j+n
        return decoded_string
    

# alternate way:

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:  # (if strs == []:)
            return 'EMPTY_LIST'
        s = "\x1f".join(strs)
        print(s)
        return s
    
    def decode(self, s: str) -> List[str]:
        if s == 'EMPTY_LIST':
            return []
        elif s == "":
            return [""]
        else:
            de = s.split('\x1f') 
            print("de val:", de)
            return de

