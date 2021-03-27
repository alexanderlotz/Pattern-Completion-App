import os
import sys
import math


def linear_test(numbers):
    first = int(numbers[0])
    second = int(numbers[1])
    difference = second - first
    for i in range(0, len(numbers) - 1):
        if int(numbers[i]) + difference == int(numbers[i + 1]):
            continue
        else:
            return False
    return difference


def geometric_test(numbers):
    first = int(numbers[0])
    second = int(numbers[1])
    if second == 0:
        return 0
    scalar = second / first
    for i in range(0, len(numbers) - 1):
        if int(numbers[i]) * scalar == int(numbers[i + 1]):
            continue
        else:
            return False
    return scalar


def find_sequence(numbers):
    lin_test = linear_test(numbers)
    geom_test = geometric_test(numbers)
    if not linear_test == "False":
        return "number is linearly increasing at an addition of: " + str(lin_test)
    elif not geom_test == "False":
        return "number is geometrically increasing at a factor of: " + str(geom_test)
    else:
        return "numbers do not seem to exhibit a pattern"


print(find_sequence("642"))
print(find_sequence("1234567"))
print(find_sequence("7654321"))
print(find_sequence("69438"))
print(find_sequence("0000000"))
print(find_sequence("1248"))
