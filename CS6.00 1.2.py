#Problem Set 1 #2
#Name: Margaret Retzinger
#Collaborators: Damien Retzinger
#Time: 00:30
#

import math

currentNumber = 3
primes = [2]
sumLogs = 0
n = 100`

while(currentNumber <= n) :
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

for prime in primes :
    sumLogs += math.log(prime)
print('Sum of the logs of the primes: ',sumLogs)
print('n: ', n)
print('ratio: ', (sumLogs/n))