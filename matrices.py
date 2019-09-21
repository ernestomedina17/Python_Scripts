#!/usr/bin/python
import sys


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
        print("How many rows does the Matrix have?")
        rows = int(raw_input('---> '))
        print("How many columns does the Matrix have?")
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

    @staticmethod
    def substract(a, b):  # Pass 2 matrices as arguments
        array = list()  # Declare empty list
        row = list()  # Declare empty list
        print("\nBoth Matrices will be substracted")
        for r in range(a.rows):
            for c in range(a.cols):
                element = a.array[r][c] - b.array[r][c]
                row.append(element)
            array.append(tuple(row))  # Append the row as an immutable tuple
            row = []  # Clear the row
        return a.rows, a.cols, array  # Returns a tuple

    @staticmethod
    def multiply(a, b):  # Pass 2 matrices as arguments
        if a.cols != b.rows:
            sys.exit('listofitems not long enough')
        array = list()  # Declare empty list
        row = list()  # Declare empty list
        tmprow = list()  # Declare empty list
        rowsum = 0
        print("\nBoth Matrices will be multiplied")
        for ar in range(a.rows):
            temparow = a.array[ar]
            for bc in range(b.cols):
                for br in range(b.rows):
                    element = temparow[br] * b.array[br][bc]
                    row.append(element)
                    rowsum += element
                tmprow.append(rowsum)
                print(str(row) + " = " + str(rowsum))
                row = []
                rowsum = 0
            array.append(tuple(tmprow))
            tmprow = []
        return a.rows, b.cols, array  # Returns a tuple


def main():
    # Instantiate the object by typing in the Matrix numbers
    # A = Matrix(*Matrix.type_matrix())  # The * Expand the tuple as arguments
    # A.print_matrix()

    matrix_a = [(-3, 2, 1, 4),
                (2, 5, 3, -2)]

    matrix_b = [(-3, 2, 1, 4),
                (2, 5, 3, -2)]

    A = Matrix(2, 4, matrix_a)
    B = Matrix(2, 4, matrix_b)
    A.print_matrix()
    B.print_matrix()

    # Add 2 matrices
    D = Matrix(*Matrix.add(A, B))
    D.print_matrix()

    print("\n----------------------------------------------------------------")

    # Substract 2 matrices
    D = Matrix(*Matrix.substract(A, B))
    D.print_matrix()

    print("\n----------------------------------------------------------------")

    # Multiply the matrix by a number
    E = Matrix(*A.multiply_number())
    E.print_matrix()

    print("\n----------------------------------------------------------------")

    # Matrix C which can be multiplied to Marix A
    matrix_c = [(0, -4, 1),
                (1, -2, 1),
                (2, 0, 2),
                (3, 2, 1)]

    C = Matrix(4, 3, matrix_c)
    A.print_matrix()
    C.print_matrix()

    # Multiply 2 Matrices, rows from A == cols from B
    # And C would result in A rows x B columns size
    F = Matrix(*Matrix.multiply(A, C))
    F.print_matrix()


if __name__ == '__main__':
    main()
