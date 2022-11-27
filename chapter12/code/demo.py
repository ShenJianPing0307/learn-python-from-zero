def write_file():
    with open("demo.csv", mode="w") as f:
        for i in range(1000):
            f.write(f"aaa{i}\n")


def get_lines():
    with open("demo.csv") as f:
        for i in f:
            yield i


# write_file()
gl = get_lines()
for i in gl:
    print(i, end="")
