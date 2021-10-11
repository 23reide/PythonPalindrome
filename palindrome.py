import random as r
import math

numbers = []
found = []

def findPalindromes(length):
    i = 0
    while(i < len(numbers)-length):
        halfLength = math.floor(length/2)

        left = []
        j = i
        while(j-i < halfLength):
            left.append(numbers[j])
            j += 1

        right = []
        j = length + i - 1
        while(j > length + i - 1 - halfLength):
            right.append(numbers[j])
            j -= 1

        if(left == right):
            j = i
            while(j-i < length):
                found.append(numbers[j])
                j += 1

        i += 1
    print(found)

def createRand(length, upBound):
    i=0
    while(i<length):
        numbers.append(r.randint(0, upBound))
        i += 1
    print("hahahahahahahahahahah")
    findPalindromes(3)

createRand(100, 20)