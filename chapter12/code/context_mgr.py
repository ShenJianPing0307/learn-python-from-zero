class File:

    def __init__(self, file_path, file_mode):
        self.file_path = file_path
        self.file_mode = file_mode

    def __enter__(self):
        print("enter")
        self.file = open(self.file_path, self.file_mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
        self.file.close()


file = File("1.csv", "r")  # 上下文管理器，上下文管理器可以使用with语句

with file as f:
    print(f.read())

# 上下文管理器 __enter__() __exit__()
# with open("1.csv") as f:
#     print(f.read())
