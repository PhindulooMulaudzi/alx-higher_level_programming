#!/usr/bin/python3

"""Main module."""

MyClass = __import__('10-my_class_2').MyClass
class_to_json = __import__('10-class_to_json').class_to_json

obj1 = MyClass("John")
obj1.win()
print(type(obj1))
print(obj1)

obj2 = class_to_json(obj1)
print(type(obj2))
print(obj2)
