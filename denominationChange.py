#!/usr/bin/python
### Greedy Algorithm
### Give money change using common denominations

denominations = [ 1, 2, 5, 10, 20, 50, 100, 500, 1000 ]
denominations.reverse()
themoney = 2193

def giveMeMyChange(money, thelist):
   myChange = []
   for VAR in thelist:
        if money < VAR:
           continue
        elif money >= VAR:
           myChange.append(VAR)
           money -= VAR
           thelist.insert(thelist.index(VAR), VAR)
   return myChange

print("The change for {0} is: {1}".format(themoney, giveMeMyChange(themoney, denominations)))
