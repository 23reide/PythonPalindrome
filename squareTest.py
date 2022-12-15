#Test if an input number is prime
#
#Get the first number
num = int(input("Enter a number:"))

def isprime (num):
    #Assume the number is prime
    isPrime = True

    #If divisible by 2 or by 3, it's not prime
    if (num % 2 == 0 or num % 3 == 0):
        isPrime = False

    else:
        #Otherwise, check only 2 numbers out of every 6, and stop when we reach the square root
        ix = 5
        while(ix * ix <= num):
            if(num % ix == 0 or num % (ix + 2) == 0):
                isPrime = False
                break
            ix = ix + 6

        #return True or False
        print(isPrime)
    #Restart
    num = int(input("Enter a number:"))
    isprime(num)

#Run the program
isprime(num)
