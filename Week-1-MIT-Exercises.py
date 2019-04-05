'''
Week 1 MIT Exercises: Core Elements of Programming
Conditionals, Branching and (for and while) Loops
'''

#Exercise 1: Write a piece of Python code that prints out the string 'hello world' if the value of an integer variable, happy, is strictly greater than 2.

happy = 1
if happy > 2:
    print("hello world")
else:
    print("goodbye world")

#Exercise 2: Write a piece of Python code that evaluates varA and varB, and then prints out one of the following messages...
    
varA = 3
varB = 5
string = "hello"
if varA !=string or varB != string:
    	print("string involved")
if varA > varB:
        print("bigger")
if varA == varB:
        print("equal")
if varA < varB:
        print("smaller")
		
#Exercise 1: Convert the following into code that uses a while loop.

n=0
while (n < 10):
    print('print ' + str(n))
    n += 2
    
print("Goodbye!")

#Exercise 2: Convert the following into code that uses a while loop.

n = 10
print('Hello!')
while (n > 1):
	print('prints ' + str(n))
	n -= 2

'''Exercise 3: Write a while loop that sums the values 1 through end, inclusive. end is a variable that 
we define for you. So, for example, if we define end to be 6, your code should print out 
the result:
21
which is 1 + 2 + 3 + 4 + 5 + 6.
'''
end = 14
i = 1
result = 0
while i <= end:
    result += i
    i += 1

print(result)
    
#end, iterator, result. (Got some help)

#for loops exercises:

#Exercise 1: Convert the following code into code that uses a for loop.

for n in range(2,12,2):
	print('prints ' + str(n))
print('Goodbye!')

#Exercise 2: Convert the following code into code that uses a for loop.

print('Hello!')
for n in range(10,0,-2):
       if n <= 10:
           print(n)
           
'''
Alternative:

num = ['hello', 10,8,6,4,2]
for i in num:
    if n <=10:
        print(n)
    else:
        n = 2
        break
'''
           
'''
Exercise 3: Write a while loop that sums the values 1 through end, inclusive. end is a variable that 
we define for you. So, for example, if we define end to be 6, your code should print out 
the result:
21
which is 1 + 2 + 3 + 4 + 5 + 6.
'''
        
sum = 0
i = 1
end = 3
for i in range(i,end+1):
    sum += i
print(sum)

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
