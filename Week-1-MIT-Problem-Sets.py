'''
Week 1 problem sets

1. Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', 
your program should print:
    
Number of vowels: 5
'''
count = 0
s = 'a', 'e', 'i', 'o', 'u'
for letter in 'Alphabet':
    if letter in s :
            count += 1
            
print('count is equal to ' + str(count))
            
#s is equal to the count.

'''
2. Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print:
    
Number of times bob occurs is: 2
'''

count = 0
word = 'bobcatbobcatbobcat'
s = 'bob'
a = word.count(s)
        
print('Number of times bob occurs is: ' + str(a))
