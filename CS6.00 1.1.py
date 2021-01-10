#Problem Set 1 #1
#Name: Margaret Retzinger
#Collaborators: Damien Retzinger
#Time: 02:30
#
#Computes 1000th prime number

currentNumber = 3
primes = [2]
n = 1000

while(len(primes) < n) :
    isPrime = False
    for prime in primes :
        #checks that the current number is not divisible by the current prime number
        if currentNumber % prime != 0 :
            isPrime = True
        else :
            #current is definitely composite so we move on
            isPrime = False
            break
    if isPrime :
        primes.append(currentNumber)
    currentNumber += 1
print(primes[-1])