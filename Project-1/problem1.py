'''Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
 For example, if s = 'azcbobobegghakl', your program should print:'''

s = 'azcbobobegghakl'
count = 0
for vowel in s:
  if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel =='o' or vowel == 'u':
     count += 1
     
print("Number of vowels: " + str(count))