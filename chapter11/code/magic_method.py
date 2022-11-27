
# f[key]
class FactoryDict:

    def __init__(self):
        self.dict = {}

    def __getitem__(self, item):
        print("__getitem__")
        return self.dict.get(item)

    def __setitem__(self, key, value):
        print("__setitem__")
        self.dict[key] = value

    def __delitem__(self, key):
        print("__delitem__")
        del self.dict[key]

    def __len__(self):
        print("__len__")
        return len(self.dict)

fd = FactoryDict()

# fd.name = "zhangsan"
fd["name"] = "zhangsan"
print(fd["name"])
