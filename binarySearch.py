#!/usr/bin/python
### Divide and Conquer Algorithm
### Binary Search

def binarySearch(alist, item):
   first = 0
   last = len(alist)-1
   found = False

   while first <= last and not found:
      midpoint = (first + last)//2
      if alist[midpoint] == item:
         found = True
      else:
         if item < alist[midpoint]:
            last = midpoint - 1
         else:
            first = midpoint + 1
   return found

thelist = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
print(thelist)
print("Is the number 66 present?: {}".format(binarySearch(thelist, 66)))
print("Is the number 77 present?: {}".format(binarySearch(thelist, 77)))
