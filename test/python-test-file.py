# From: https://www.youtube.com/watch?v=06I63_p-2A4

import sys


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(sys.version)

print(greet("World"))

print(sys.executable)

print(greet("Tomas"))

