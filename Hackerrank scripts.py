# #Polar Coordinates
#
# import cmath
#
# cnum = input('Enter complex number a+ij: ')
#
# #complex(input())
#
# polarcoord = cmath.polar(complex(cnum))
#
# for n in polarcoord:
#     print(round(n,3))


# #Average of distinct numbers from a given set of numbers
# def average(array):
# # your code goes here
#     distinctset = set(array)
#     distinctnum = len(distinctset)
#     return (sum(distinctset)/distinctnum)
#
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)

#Given  sets of integers,  and , print their symmetric difference in ascending order.
# The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

# if __name__ == '__main__':
#     n = int(input())
#     l1 = list(map(int, input().split()))
#     setn=set(l1)
#     m = int(input())
#     l2=list(map(int, input().split()))
#     setm=set(l2)
#
#     symmdiff = list((setn.union(setm)).difference((setn.intersection(setm))))
#     symmdiff.sort()
#     for i in symmdiff:
#         print (i)

'''
There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers.
You like all the integers in set A and dislike all the integers in set B.
Your initial happiness is 0. For each i integer in the array, if i E A , you add 1 to your happiness.
If i E B, you add -1 to your happiness. Otherwise, your happiness does not change.
Output your final happiness at the end.
'''

# if __name__ == '__main__':
#     n,m = map(int, input().split())
#     numlist = list(map(int, input().split()))
#     setA = set(map(int, input().split()))
#     setB = set(map(int, input().split()))
#     happiness = 0
#
#     for i in numlist:
#         if i in setA:
#             happiness += 1
#         elif i in setB:
#             happiness -= 1
#
#     print (happiness)

#########################################################################
# if __name__ == '__main__':
#     n = int(input())
#     stamplist = []
#     for i in range(n):
#         country = input()
#         stamplist.append(country)
#
#     print(len(set(stamplist)))
#########################################################################

# from collections import defaultdict
# if __name__ == '__main__':
#     n,m = map(int, input().split())
#
# A = []
# B = []
# for i in range(n):
#     word = input()
#     A.append(word)
# for j in range(m):
#     word = input()
#     B.append(word)
#
# d=defaultdict(list)
# for w in B:
#     if w in A:
#         w_index = [i for i,x in enumerate(A,1) if x==w]
# #        print(w_index)
#         for x in w_index:
#             d[w].append(x)
#     else:
#         if w not in d:
#             d[w].append(-1)
# #    print (w+' done')
#
# print (d)
# for i,v in d.items():
#     print (*v)
# for j in v:
#       print (*j)
#    print()

#####  NAMED TUPLE  ######

from collections import namedtuple
student=namedtuple('student','ID MARKS CLASS NAME')

stunum = int(input())
markidx = list(input().split()).index('MARKS')

totalmarks = 0

for m in range(stunum):
    totalmarks += int(list(input().split())[markidx])

print (round(totalmarks/stunum,2))

#####  NAMED TUPLE  ######
#####  ORDERED DICTIONARY  ######

from collections import OrderedDict

items=int(input())







