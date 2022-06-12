'''Write a program that prints the number of times the string 'bob' occurs in s.
 For example, if s = 'azcbobobegghakl', then your program should print'''

index = 0
count = 0
for bob in s:
   if s[index:(index + 3)] == 'bob':
     count += 1
   index += 1
   
print('Number of times bob occurs is: ' + str(count))  