class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # word abbreviation
       
        # not be adjacent , not empty substrings , lenght shouldnt have leadings 0s
        # string 
         # word == abr 

# Goal of the problem : numbers are used to skip letters in the word. 

        # use two pointer 
        word_index = 0
        abbr_index = 0

        # 2 things need to check :
            # 1. is it a "digit" in abbr 
            # 2. is it a "alphabet" in abbr that matches with the word 
        
        # checking they are inside the range (using while condition)

        while word_index < len(word) and abbr_index < len(abbr): 

            if abbr[abbr_index].isdigit():
                move = 0 # its declared to count the moves to be parsed (moved) the chars/letters in word 

                if abbr[abbr_index] == '0': #  checking the string 0 not the int 0 
                    print("0 index:",abbr[abbr_index])
                    return False
                
                while abbr_index < len(abbr) and abbr[abbr_index].isdigit():
                    move = move * 10 + int(abbr[abbr_index])

                    abbr_index += 1

                    # 0 + 1 = 1  move =1
                    # 10 + 2 = 12 move = 12... 
                    # stop here
                    # 120 + 
                # use move to prerform in word 
                word_index += move 
                # word_index = 0
                # 0+12 = 12 word_index = 12

             # 2. is it a alphabet 

            else:
                if word[word_index] != abbr[abbr_index]:
                    return False
                word_index+=1
                abbr_index+=1


           

            
            
        return word_index==len(word) and abbr_index == len(abbr)

# Time - O(n) , Space - O(1)
