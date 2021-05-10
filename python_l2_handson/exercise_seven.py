class First():

    def method1():
        print("First")


class Second(First):

    def __init__(self) -> None:
        super().__init__()

    def method1():
        print("second")


class Third(First):

    def __init__(self) -> None:
        super().__init__()

    def method1():
        print("Third")


class Fourth(Second, Third):

    def __init__(self) -> None:
        super().__init__()

    def method1():
        print("Fourth")


r = Fourth()
print(Fourth.__mro__)
