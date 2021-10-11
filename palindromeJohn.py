import random as r
import math

numbers = []
found = []

def findPalindromes(length):
    i = 0
    while(i < len(numbers)-length):
        j=0
        while(numbers[i+j] == numbers[(i+length-1)-j]):
            j += 1
            if(j >= length//2):
                k=0
                while(k < length):
                    found.append(numbers[k+i])
                    k += 1
                i += 1
        i += 1
    print(found)

def createRand(length, upBound):
    i=0
    while(i<length):
        numbers.append(r.randint(0, upBound))
        i += 1
    print(numbers)
    findPalindromes(2)

createRand(100, 20)
