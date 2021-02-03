#Problem Set 2 (Part I)
#Name: Margaret Retzinger
#Collaborators: 
#Time: 


# def nuggets(n) :
#     for a in range(1,100) : 
#         for b in range(1,100) :
#             for c in range(1,100) :
#                 n = 6*a + 9*b +20*c
#                 print(n)


def nuggets(n) :
    a = 0
    b = 0
    c = 1
    # if n == 6*a + 9*b +20*c :
    #     print(n, ' : ', a, b, c)
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

    # for a in range(1,100) : 
    #     for b in range(1,100) :
    #         for c in range(1,100) :
                


print(nuggets(50))

n = 1
nList = []

# while nList.len() <= 6 :
#     n = 6*a + 9*b +20*c

#print('Largest number of McNuggets that cannot be bought in exact quantity: ', n)

