class MyList(list):

    def __init__(self, *args, **kwargs):
        super(MyList, self).__init__(*args, **kwargs)

    def __getitem__(self, item):
        return super(MyList, self).__getitem__(item) + 2


ml = MyList([1, 2, 3])
print(ml[1])