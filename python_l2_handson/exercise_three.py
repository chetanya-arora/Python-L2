c = 0


def f2(x):
    try:
        c += 1
        b = x + c
        print(c)
        return b
    except UnboundLocalError as error:
        print(error)


print(f2(1))
print(c)
