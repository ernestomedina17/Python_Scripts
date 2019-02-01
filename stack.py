#!/usr/bin/python

class EmptyStackError(Exception):
   """ Custom Error for empty stack."""
   pass #pass is a null operation -- when it is executed, nothing happens.

class Stack:
    """ Stack: LIFO Data Structure. Operations: push(item), pop(), peek(), isEmpty(), size() """
    def __init__(self):
       """ Define an empty stack. Here we are using a list to implement the Stack data structure. """
       self._list = []  ## Items in the stack
       self._top = -1   ## Denotes the top of the stack

    def isEmpty(self):
       """ Test if the stack has no items.
           :return: True if the Stack is Empty. False otherwise """
       return self._top == -1

    def push(self, item):
       """ Pushes an item at the top of the stack updating the top of the stack.
           :param items: item to be added on the stack """
       self._list.append(item)
       self._top += 1

    def pop(self):
       """ Removes an item from the top of the stack modifying it.
           :return: item removed from the top of the stack.
           :raises: EmptyStackError if stack has no elements. """
       if self.isEmpty():
          raise EmptyStackError("Stack is Empty: Trying to pop from an empty stack")
       self._top -= 1
       return self._list.pop()

    def peek(self):
        """ Just returns the item at the top of the stack without modifying the stack.
            :return: item at the top of the stack.
            :raises: EMptyStackError if stack has no elements. """
        if self.isEmpty():
            raise EmptyStackError("Stack is Empty: Trying to peek into an empty stack")
        return self._list[self._top]

    def size(self):
         """ Returns the number of elements currently in the stack.
             :return: size of the stack. """
         return self._top + 1  ## 0 index + 1

if __name__ == "__main__":
    s = Stack()
    s.push("Hello")
    s.push("world")
    s.push("This ")
    s.push("is ")
    s.push("a beautiful day")

    print("Size of the Stack is: {}. Element at the top is: {}".format(s.size(), s.peek()))
    print(type(s._list))
    print(type(s._top))


    while not s.isEmpty():
        print(s.pop())

    import time
    time.sleep(1)  ## To ensure output from program and Exception is not interleaved.

    #Try to pop from an empty stack.
    s.pop()
