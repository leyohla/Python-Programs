'''
Following along with the Python exercises set by thenewboston's YouTube videos.
'''

#infinite loops:

#Input:
num = int(input("type a number: "))
print(num)

Output: 
Type a number: 

#While Loop:
while 1:
    number = input('Enter number: ')
    if number == '4': break
Output:
Enter number: 
Enter number:
Enter number:

#Asks for user input before each iteration, and loops once user inputs a number.

#Dictionaries:

ages = {'me': 22, 'someone': 32, 'someoneelse': 65}
for item in ages:
    print item
    
Output: 
me
someone
someoneelse
