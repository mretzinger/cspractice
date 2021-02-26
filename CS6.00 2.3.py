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

# def nuggets(n) :
#     for a in range(1,100) : 
#         for b in range(1,100) :
#             for c in range(1,100) :
#                 n = 6*a + 9*b +20*c
#                 print(n)


def nuggets() :
    a = 0
    b = 0
    c = 0
    n=1
    while n < 60 : 
        if n == 6*a + 9*b +20*c :
            print(n, ' : ', a, b, c)
    # for a in range(0, 10) :
    #     if n == 6*a + 9*b +20*c :
    #         print(n, ' : ', a, b, c)
    #         for b in range(0,10) :
    #             if n == 6*a + 9*b +20*c :
    #                 print(n, ' : ', a, b, c)
    #                 for c in range(0,10) :
    #                     if n == 6*a + 9*b +20*c :
    #                         print(n, ' : ', a, b, c)

    for a in range(0,10) :
        #if n == 6*a + 9*b +20*c :
        #print('test', b) #n, ' : ', a, b, c)
        for b in range(0,10) :
            if n == 6*a + 9*b + 20*c :
                print('works') #n, ' : ', a, b, c)
            if n == 6*a + 9*b +20*c  : 
                print('success', a, b, 6*a + 9*b + 20*c)
    print('Largest number of McNuggets that cannot be bought in exact quantity: ', n)

    # for a in range(1,100) : 
    #     for b in range(1,100) :
    #         for c in range(1,100) :
                


print(nuggets())

# n = 1
# nList = []

# while nList.len() <= 6 :
#     n = 6*a + 9*b +20*c


