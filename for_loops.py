import time
# for loops: a statement that will execute it's block of code a limited amount of times
# while loop = unlimited
# for loop = limited

for i in range(10): #for every number in the range of 10, print that number plus 1
    print(i + 1)

print('------------------------------------------')

for i in range(50,100+1, 5): # for every ifth number between 50 and 1000, print that number
    print(i)

print('------------------------------------------')


for i in "Suhruth Chamarthi": # for every character in my name (including the space), print character
    print(i)

print('------------------------------------------')


for seconds in range(10,0,-1): # for every number from 10 to 0, count down every one second then print Happy New Year
    print(seconds)
    time.sleep(1) #loop waits one loop before running again
print('Happy New Year!')