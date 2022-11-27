import flask.globals

# class Local(object):
#
#     def __init__(self):
#         object.__setattr__(self, '__storage__', {})
#         object.__setattr__(self, '__ident_func__', get_ident)
#
#     def __getattr__(self, name):
#         try:
#             return self.__storage__[self.__ident_func__()][name]
#         except KeyError:
#             raise AttributeError(name)
#
#     def __setattr__(self, name, value):
#         ident = self.__ident_func__()
#         storage = self.__storage__
#         try:
#             storage[ident][name] = value
#         except KeyError:
#             storage[ident] = {name: value}
#
#     def __delattr__(self, name):
#         try:
#             del self.__storage__[self.__ident_func__()][name]
#         except KeyError:
#             raise AttributeError(name)


# local_values = Local()


class Animal(object):

    def __init__(self):
        object.__setattr__(self, '__storage__', "")
        # self.__storage__ = ""

    def __setattr__(self, key, value):  # self.__dict__[key] = vale
        print("__setattr__", key, value)
        pass

    def __getattr__(self, item):  # return self.__dict__[key]
        print("__getattr__", item)
        pass

    def __delattr__(self, item):  # self.__dict__[item] = None
        print("__delattr__", item)
        pass


animal = Animal()

animal.name = 'xh'

print(animal.__storage__)
