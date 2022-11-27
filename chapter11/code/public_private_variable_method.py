class Bar:

    a = 10
    __b__ = 20
    __c = 30
    _d = 40

    def get_c(self):
        print(self.__c)

print(Bar._Bar__c)
# print(Bar.a)
# print(Bar.__b__)
# print(Bar._d)
# print(Bar.__c) # AttributeError: type object 'Bar' has no attribute '__c'

# bar = Bar()
# bar.get_c()
