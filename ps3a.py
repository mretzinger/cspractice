#Problem Set 3.1

# Write two functions, called countSubStringMatch and countSubStringMatchRecursive that
# take two arguments, a key string and a target string. These functions iteratively and recursively count
# the number of instances of the key in the target string. You should complete definitions for
# def countSubStringMatch(target,key):
# and
# def countSubStringMatchRecursive (target, key): 


from string import *

def countSubStringMatch(target, key) :
    if find(target, key) == -1 :
        return 0
    else :
        return find(target, key)


def countSubStringMatchRecursive(target, key) :



