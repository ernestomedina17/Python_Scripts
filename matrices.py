#!/usr/bin/python 

class Matrix:
  def __init__(self, rows, cols, array):
    self.rows = rows
    self.cols = cols
    self.array = array
  def printMatrix(self):
    print("\nYour Matrix:  ")
    for r in range(self.rows):
      print(self.array[r])
  @staticmethod
  def typeinMatrix():
    print("How many rows does Matrix A Have?") 
    rows = int(raw_input('---> '))
    print("How many columns does Matrix A Have?") 
    cols = int(raw_input('---> '))
    array = list() # Declare empty list
    row = list()   # Declare empty list
    print("Capture the Matrix A elements")
    for r in range(rows):
      for c in range(cols):
        element = int(raw_input('[' + str(r) + '][' + str(c) + ']--->'))
        row.append(element)
      array.append(tuple(row)) # Append the list as an immutable tuple
      row = [] #clear the list 
    return rows, cols, array #Returns a tuple
    
def main():
  # Instantiate the object
  A = Matrix(*Matrix.typeinMatrix()) #The * Expand the tuple as arguments
  A.printMatrix()

if __name__ == '__main__':
    main()
