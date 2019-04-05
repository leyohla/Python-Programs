#if-else

x = 4
y = 8
if x == y:
    print('x and y are equal')
    if y !=0:
        print('therefore x/y is', x/y)
    
elif x > y:
    print('x is bigger than y')
else:
    print('y is bigger')
    
#while loops - unlimited iterations unless n is initialised.

b= 5
b
while b <= 10:
    print(b)
    b += 1

n = input("rubiks cube")
while n == "right":
    n = input("turn to the right")
print("you have solved the cube")

n = 0
while(n < 8):
    print(n)
    n = n+2
    
#output: 0, 2, 4, 6

#for loops - we know the amount of iterations.

for n in range(1,11,3):
    print(n)
#outputs: 1,4,7,10
#range(start, stop, step)
    
sum = 12

for i in range(5,10):
    sum += i
    print(sum)
#for the first multiple of 5 up from 12...adds 5 to 12 to make 17, then increments by the sum.
    
sum = 9

for i in range(5,10):
    sum += i
    print(sum)
#output: 14,20,27,35,44. Increments by all values before 10, so 9 in this case.
    
sum = 0

for i in range(5,10):
    sum += i
    print(sum)
#output: 5,11,18,26,35
    
sum = 0

for i in range(5,11,2):
    sum += i
    if sum == 9:
        break
#output: 5+7=12,+9=21. The sum doesn't reach 9 so it breaks at 12+9. 
        
sum = 0

for i in range(5,11,2):
    sum += i
    if sum == 12:
        break
#output: 5+7=12. Code reaches 12 on second iteration of loop so breaks at 12.
