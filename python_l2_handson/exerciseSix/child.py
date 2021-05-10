from parent import Parent


class Child(Parent):

    def __init__(self) -> None:
        super().__init__()


a = Child()

print(a.addition(10, 20))
print(a.subtraction(10, 20))
print(a.multiplication(10, 20))
print(a.division(10, 20))
print(a.sqroot(100))
