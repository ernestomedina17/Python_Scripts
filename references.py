#!/usr/bin/python

i = [1,2,3]
j = i
i[0] = 5

print("i {}".format(i))
print("j {}".format(j))
print("-------------------- j references to i")
j[0] = 6

print("i {}".format(i))
print("j {}".format(j))
print("-------------------- j still references to i")

j = [7,2,3]

print("i {}".format(i))
print("j {}".format(j))
print("-------------------- j references to a new object")
