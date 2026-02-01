def z1_function():
    print("This is z1 function")


# z1_function()


x = "x from z1"


def z1_outscoped():
    print(x)





# demonstrational example of readability of 
# script/module behavior


def do_smth(awas: None) -> list[int]:
    print('doing smth')
    return [123]

def do_smth_else() -> None:
    print('doing smth else')


def main() -> None:
    do_smth(None)
    do_smth_else()



if __name__ == "__main__":
    main()
    print("Z1 RUN")
