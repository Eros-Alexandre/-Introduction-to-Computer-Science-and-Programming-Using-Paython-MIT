'''Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example,
 if s = 'azcbobobegghakl', then your program should print'''



s = "ixislbqzulosrlwzr"
alphabet = "abcdefghijklmnopqrstuvwxyz"
LongestString = ""
string = s[0]
for i in range(len(s) - 1):
    if alphabet.index(s[i]) <= alphabet.index(s[i + 1]):
        string += s[i + 1]
        if len(string) > len(LongestString):
           LongestString = string
    else:
        string = s[i + 1]
if len(LongestString) == 0:
    LongestString = s[0] 
print('Longest substring in alphabetical order is: ' + LongestString)



    

   
   
         

    
        
    




















            

    
    
