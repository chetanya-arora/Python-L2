def fibonacciGenerator(num):
    a = 0
    b = 1
    for i in range(num):
        yield b
        a, b = b, a+b


obj = fibonacciGenerator(10)

# print line by line fibonacci numbers
for i in obj:
    print(i)
