class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # fisrt pass is for checking closing paraenthesis 
    
        countOpeningPara = 0
        
        result = []

        for i in range(len(s)):
            
            # if s[i] == ')':
            #     s[i].pop()
            if s[i] == '(' :
                countOpeningPara += 1
                result.append(i)
            elif s[i] == ')': 
                if countOpeningPara > 0:
                     # its valid if matching opening paraenthesis are found 
                    countOpeningPara -= 1 
                    result.append(i)


            else:
                result.append(i)

        

        # second pass to check for opening parenthesis 

        finalResult = []
        countClosingPara = 0
        for i in result[::-1]:
            # why reveresed?
            # [lee(t)()(ode(]
            if i == ')':
                countClosingPara +=1
                finalResult.append(i)
            elif i == '(': 
                # check does the open parenthesis has the match - close paraenthesis 
                if countClosingPara > 0:
                    countClosingPara-=1
                    finalResult.append(i)
                   
            else:
                finalResult.append(s[i])

        return ''.join(finalResult[::-1])


            