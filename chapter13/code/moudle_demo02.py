from handle_name import get_name


class Animal:

    def __init__(self):
        self.name = "lily"


def main():
    a = Animal()
    res = get_name(a.name)
    print(res)


main()
