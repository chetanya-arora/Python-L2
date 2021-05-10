def test_keyboardInturuppted():
    try:
        print("your name")
        print("Press ctrl+c")
        name = input()
        print(f"Welcome aboard {name}")
    except KeyboardInterrupt:
        print("Keyboard intrupted, Please run the program again this time no ctrl+c, just your name")
    finally:
        print("KeyboardInterrupt Passed")


def test_nameError():
    try:
        print("Your name")
        name = input()
        prin(name)
    except NameError:
        print("It should be print, found prin")
    finally:
        print("NameError Passed")


def test_arithmaticError():
    try:
        print(10/0)
    except ArithmeticError:
        print("Can't divide with zero")
    finally:
        print("ArithmeticError Passed")


# Tests whether KeyboardInterrupt passes or not
test_keyboardInturuppted()

# Tests whether NameError passes or not
test_nameError()

# Tests whether ArithmaticError passes or not
test_arithmaticError()
