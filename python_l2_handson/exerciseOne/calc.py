import math as m


def factorial(num):
    try:
        if num <= 1:
            return num
        return num * factorial(num-1)
    except TypeError:
        return "String is not supported, Input a number"


def log10(num):
    try:
        return m.log10(num)
    except TypeError:
        return "String is not supported, Input a number"


def radian(num):
    try:
        return m.radians(num)
    except TypeError:
        return "String is not supported, Input a number"


def sin(num):
    try:
        return m.sin(num)
    except TypeError:
        return "String is not supported, Input a number"


def cos(num):
    try:
        return m.cos(num)
    except TypeError:
        return "String is not supported, Input a number"


def tan(num):
    try:
        return m.tan(num)
    except TypeError:
        return "String is not supported, Input a number"
