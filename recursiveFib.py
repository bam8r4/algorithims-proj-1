#Author of this code:Brent Moran
#This code outputs the nth fibonacci number by computing it recursively and outputs the time required to reach that result.
#I am importing time to measure how long the execution takes.
import time

#Prompt the user for an input.
print("Input value for N: ")

#Taking input from the user to determine which fib number to solve for.
N = input()

def recur(N):
    if N < 0:
	print("That is not a correct input")

    elif N == 0:
        return 0

    elif N == 1:
        return 1

    elif N==2:
	return 1

    else:
	return recur(N-1) + recur(N-2)


#We will start the timer before and end it after the execution of the function is completed.
start = time.time()
print("The result is:")
print(recur(N))
end = time.time()

print("The time required in seconds for this size input is: ")
print(end-start)

