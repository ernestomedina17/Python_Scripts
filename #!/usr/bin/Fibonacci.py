#!/usr/bin/python
### Fibonacci Algorithm using Dynamic Programming

def fibonacci(n, lookup):
   if n == 0 or n == 1:
      lookup[n] = 1
   if lookup[n] is None:
      lookup[n] = fibonacci(n-1, lookup) + fibonacci(n-2, lookup)
   return lookup[n]

if __name__ == "__main__":
   for VAR in range(1, 40):
      lookup = [None]*(VAR+1)
      print("Fibonacci using DP {} ".format(fibonacci(VAR, lookup)))
      print(lookup)
