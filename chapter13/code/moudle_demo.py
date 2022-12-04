import handle_name
class Animal:

    def __init__(self):
        self.name = "lily"


def main():
    a = Animal()
    res = handle_name.get_name(a.name)
    print(res)



main()
