#Author of this code:Brent Moran
#Used to find the nth fibonacci number through iteration. The time required will be outputted. 
#Importing time to check to see how long it takes to run.
import time

#Function for iteration.
def iterate(N):

    first = 0
    second = 1
    third = second + first

#We are assuring that the input is positive.
    if N < 0:
	print("That value is not valid. Make sure its a positive integer.")
    elif N == 0:
        return 0
    elif N == 1:
        return 1
    elif N == 2:
        return 1
    else:
	for x in range (1,N):
            temp = second + first
            first = second
            second = temp 
            third = temp

        return third


#Prompting user	for input.
print("Input value")
N = input()

#Starting timer	to measure how long it takes.
start = time.time()
print(iterate(N))
end = time.time()

print("The time required in seconds was")
print(end - start)

