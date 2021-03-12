#Problem Set 2 (Part 3)
#Name: Margaret Retzinger
#Collaborators: Damien Retzinger
#Time: 

#“Largest number of McNuggets that cannot be bought in exact quantity: <n>” 

# Hypothesize possible instances of numbers of McNuggets that cannot be purchased
# exactly, starting with 1
# For each possible instance, called n,
# Test if there exists non-negative integers a, b, and c, such that
# 6a+9b+20c = n. (This can be done by looking at all feasible
# combinations of a, b, and c)
# If not, n cannot be bought in exact quantity, save n
# When you have found six consecutive values of n that in fact pass the test of
# having an exact solution, the last answer that was saved (not the last value
# of n that had a solution) is the correct answer, since you know by the
# theorem that any amount larger can also be bought in exact quantity 


def nuggets() :
    n=1
    largestNotPurchasable = n

    while n < 60 : 
        if(notPurchasable(n)):
            largestNotPurchasable = n
        n = n + 1

    return largestNotPurchasable

def notPurchasable(n): 
        for a in range(0,10) :
            for b in range(0,6) :
                for c in range (0,2) :  
                    # If there is a solution, then the number of nuggets "n" is purchasable.
                    if n == 6*a + 9*b + 20*c : 
                        # We need to move on to the next number "n".
                        return False
                    
        return True

print('Largest number of McNuggets that cannot be bought in exact quantity: ', nuggets())


