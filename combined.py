#Author of this code:Brent Moran
#This will compare running times of calculating the nth fibonacci number using both recurions and an iterative approach.

import time

#Defing the function for iteration.
def iterate(N):

    first = 0
    second = 1
    third = second + first
	
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

#Defining the function for recursion.
def recur(N):	
    if N < 0:
	print("That value is not valid. Make sure its a positive integer.")
    elif N == 0:
        return 0
    elif N == 1:
        return 1
    elif N == 2:
        return 1
    else:
	return recur(N-1) + recur(N-2)
print("\n\nInput value")
N = input()

#Measuring the time it takes for the iterative function to complete.
start = time.time()
print(iterate(N))
end = time.time()

#Output the time it took for the iterative function.
print("The time required in seconds using iteration was")
print(end - start)

#We are giving this variable a value so we can compare it to the other functions time later.
iterTime = end - start

print("We are now running the recursive algorithim...hold on this could take a while")

#Starting the timer again for the recursive function.
start = time.time()
print(recur(N))
end = time.time()

print("The time required in seconds using iteration was")
print(end - start)

#This value will be compared against iterTime to see which ran faster.
recurTime = end - start


print("Now we will compare the time it took for each algorithm to complete\n")

#Print which time was faster and by how much.
if iterTime < recurTime:
    print("The algorithim using iteration finished faster than recursion")
    print("The iterative algorithim finished " + str((recurTime - iterTime)) + " seconds faster")
else:
    print("The algorithim using recursion finished faster that iteration")
    print("The recursive algorithim finished " + str((iterTime - recurTime)) + " seconds faster")

print("********************************************************************************************\n")

