import sys

def add_num(a, b):
    print(a+b)

if __name__ == '__main__':
    print(sys.argv)
    _, a, b = sys.argv
    add_num(int(a), int(b))