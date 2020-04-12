import sys
import builtins
import os


def list_on_separate_lines(l):
    for elem in l:
        print(elem)


# --- Debugging functions ---
## Built ins - https://www.youtube.com/watch?v=QVdf0LgmICw
# print(dir(builtins))
## Type - https://www.geeksforgeeks.org/python-type-function/
# type()
## Id
# id()

# --- Sys ---
## Script return code
# sys.exit(100)
## Print the paths that python imports modules from - https://www.youtube.com/watch?v=CqvZ3vGoGs0&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=9
# print("--- START --- sys.path")
# system_paths = sys.path
# ## system_paths.sort()
# list_on_separate_lines(system_paths)
# print("--- END --- sys.path")

# --- OS ---
# list_on_separate_lines(dir(os))
## __ = Dunder or magic method
# print(os.__file__)
