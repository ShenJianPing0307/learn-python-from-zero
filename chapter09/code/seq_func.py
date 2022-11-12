def dynamic(p1, p2):
    print(p1)
    print(p2)


l1 = ("a", "b")
dynamic(*"ab")

def dynamic(*params):
    print("*params", *params)
    print(params) # (a, b)


l1 = ["a", "b"]
dynamic(*l1)