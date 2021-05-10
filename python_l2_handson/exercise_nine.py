class Reverser:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def reverse(self):
        if self.n > self.i:
            i = self.n
            self.n -= 1
            return i
        else:
            raise StopIteration()


s = Reverser(5)

print(s.reverse())
print(s.reverse())
print(s.reverse())
print(s.reverse())
print(s.reverse())
print(s.reverse())
