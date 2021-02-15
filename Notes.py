def solve(numLegs, numHeads):
    for numChicks in range(0, numHeads + 1) :
        numPigs = numHeads - numChicks
        totLegs = 4*numPigs + 2*numChicks
        if totLegs == numLegs: 
            return(numPigs, numChicks)
    return(None, None)


def barnYard() :
    heads = int(input('Enter num heads: '))
    legs = int(input('Enter num legs: '))
    pigs, chickens = solve(legs, heads)
    if(pigs == None) :
        print('There is no solution')
    else: 
        print('number of pigs: ', pigs)
        print('number of chickens: ', chickens)

#print(barnYard())


#Recursion
def isPalindrome(s) : #'abcdeffedcba'
    if len(s) <= 1: return True #base case
    else : return s[0] == s[-1] and isPalindrome(s[1:-1])

#fibonacci
def fib(x) :
    if x == 0 or x == 1: return 1
    else : return fib(x-1) + fib(x-2)

def add(x = 0): 
    if x<= 10:
        x = x + 1
        add(x)

#print(fib(24))


#floating point rouding errors
# a = math.sqrt(2)
# a = 1.414213562370951
# a * a == 2
# false
# a*a = 2.000000000004
#Do this instead
# abs(a*a-2.0) < epsilon
#Create a "Near" function instead of using == to compare


def squareRootBi(x, epsilon) :
    #assumes x >= 0 and epislon >0
    #return y so that y*y is within epsilon of x
    assert x >=0, 'x must be non-negaive, not ' + str(x) #assert continues if true, or stops with the statement
    assert epsilon > 0, 'epsilon must be positive, not ' + str(epsilon)
    low = 0
    high = max(x, 1.0)#incase x is less than one, instead of high = x
    guess = (low + high) / 2.0
    ctr = 1
    while abs(guess**2 - x) > epsilon and ctr <= 100 :
        #print 'low: ', low, 'high: ', high, 'guess: ', guess
        if guess**2 < x :
            low = guess 
        else : 
            high = guess
        guess = (low + high) / 2.0
        ctr += 1
    assert ctr <= 100, 'Iteration count exceeded'
    print('Bi method. Num. interations: ', ctr, 'Estimate: ', guess)
    return guess

#print(squareRootBi(0.25, 0.0001)) #This gets you an assertionError: Iteration count exceeded until we made change to line 58 high =

#print(squareRootBi(144, 0.0001)) 


def squareRootNR(x, epsilon) : #Newton-Raphson method
    #assumes x >= 0 and epislon >0
    #return y so that y*y is within epsilon of x
    assert x >=0, 'x must be non-negaive, not ' + str(x) #assert continues if true, or stops with the statement
    assert epsilon > 0, 'epsilon must be positive, not ' + str(epsilon)
    x = float(x)
    guess = x / 2.0
    diff = guess**2 - x
    ctr = 1
    while abs(diff) > epsilon and ctr <= 100 :
        #print 'Error ', diff,'guess: ', guess
        guess = guess - diff/(2.0*guess)
        diff = guess**2 - x
        ctr += 1
    assert ctr <= 100, 'Iteration count exceeded'
    print('NR method. Num. interations: ', ctr, 'Estimate: ', guess)
    return guess

unis = []
lista = ['a', 'b']
listb = ['aa', 'bb']
unis.append(lista)
unis.append(listb)
#print(unis) #list of lists

#concat flattens
unis = []
lista = ['a', 'b']
listb = ['aa', 'bb']
unis = lista + listb
#print(unis)

#Dictionaries
EtoF = {'one': 'un', 'soccer': 'football'}
#cannot print an index of a dictionary
#print(EtoF)



#Lecture 8

#goes through loop b times
def ex1(a,b) :
    ans = 1
    while (b > 0) :
        ans *= a
        b -= 1
    return ans

#Does the same thing as ex1(), but with recursion. Still linear time to solve.
def ex2(a,b) :
    if b == 1 :
        return a
    else : return a*ex2(a, b-1)

#Also the same answer as previous, 
def ex3(a,b) :
    if b == 1 :
        return a 
    if (b%2)*2 == b :
        return ex3(a*a, b/2)
    else : return a*ex3(a,b-1)


#print(ex3(3,5))

#linear
def search1(s, e) : 
    answer = None
    i = 0
    numCompares = 0
    while i < len(s) and answer == None :
        numCompares += 1
        if e == s[i] :
            answer = True
        elif e < s[i] :
            answer = False
        i += 1
    print(answer, numCompares)

#binary search logarithmic
def bsearch(s, e, first, last, calls) : 
    print(first, last, calls)
    if(last - first) < 2 :
        return s[first] == e or s[last]
    mid = first + (last - first) // 2
    if s[mid] == e :
        return True
    if s[mid] > e :
        return bsearch(s, e, first, mid - 1, calls)
    return bsearch(s, e, mid + 1, last, calls + 1)

def search(s, e) : 
    print(bsearch(s, e, 0, len(s) - 1, 1))
    print("done")

#print(search(range(1000), 9400))



#Bubble sort
def bubbleSort(L) :
    for j in range(len(L)) :
        for i in range(len(L) - 1) :
            if L[i] > L[i + 1] :
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp
        print(L)

print(bubbleSort([1,3,4,5,2,6]))

