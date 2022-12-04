from handle_name import *


class Animal:

    def __init__(self):
        self.name = "lily"


def main():
    a = Animal()
    res = get_name(a.name)
    print(res)


if __name__ == '__main__':
    main()
