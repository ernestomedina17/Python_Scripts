#!/usr/bin/python


class Matrix:
    def __init__(self, rows, cols, array):
        self.rows = rows
        self.cols = cols
        self.array = array

    def print_matrix(self):
        print("\nYour Matrix:  ")
        for r in range(self.rows):
            print(self.array[r])

    @staticmethod
    def type_matrix():
        print("How many rows does Matrix A Have?")
        rows = int(raw_input('---> '))
        print("How many columns does Matrix A Have?")
        cols = int(raw_input('---> '))
        array = list()  # Declare empty list
        row = list()    # Declare empty list
        print("Capture the Matrix A elements")
        for r in range(rows):
            for c in range(cols):
                element = int(raw_input('['+str(r)+']['+str(c)+']--->'))
                row.append(element)
            array.append(tuple(row))  # Append the list as an immutable tuple
            row = []  # Clear the list
        return rows, cols, array  # Returns a tuple

    def multiply_number(self):
        array = list()  # Declare empty list
        row = list()    # Declare empty list
        print("\nWhich number do you want the Matrix to be multiplied for?")
        multiple = int(raw_input('---> '))
        for r in range(self.rows):
            for c in range(self.cols):
                element = multiple * self.array[r][c]
                row.append(element)
            array.append(tuple(row))  # Append the list as an immutable tuple
            row = []  # Clear the list
        return self.rows, self.cols, array  # Returns a tuple

    @staticmethod
    def add(a, b):  # Pass 2 matrices as arguments
        array = list()  # Declare empty list
        row = list()  # Declare empty list
        print("\nBoth Matrices will be added")
        for r in range(a.rows):
            for c in range(a.cols):
                element = a.array[r][c] + b.array[r][c]
                row.append(element)
            array.append(tuple(row))  # Append the row as an immutable tuple
            row = []  # Clear the row
        return a.rows, a.cols, array  # Returns a tuple


def main():
    #  Instantiate the object
    A = Matrix(*Matrix.type_matrix())  # The * Expand the tuple as arguments
    A.print_matrix()
    #  Multiply the matrix by a number
    B = Matrix(*A.multiply_number())
    B.print_matrix()
    #  Add 2 matrices
    # A = Matrix(*Matrix.type_matrix())
    # B = Matrix(*Matrix.type_matrix())
    C = Matrix(*Matrix.add(A, B))
    C.print_matrix()


if __name__ == '__main__':
    main()
