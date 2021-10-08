import random as r
import math

numbers = []

def findPalindromes(length):
    i = 0
    while(i < len(numbers)):
        length = math.floor(length/2)

        left = []
        j = i
        while(j < length):
            left.append(numbers[j])
            j += 1

        right = []
        j = length + i + 1
        while(j > length//2):
            right.append(numbers[j])
            j -= 1

        if(left == right):
            found = []
            j = i
            while(j > length):
                found.append(numbers[j])
                j += 1

        i += 1

def createRand(length, upBound):
    i=0
    while(i<length):
        numbers.append(r.randint(0, upBound))
        i += 1
    print(numbers)
    findPalindromes(5)
createRand(100, 100)
