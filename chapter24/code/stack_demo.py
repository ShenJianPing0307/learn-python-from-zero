"""
1、数字（整数、复数、布尔、浮点数）
2、字符串
3、元组
4、字典
5、集合
6、列表
"""


class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def length(self):
        return len(self.items)

    def push(self, item):
        """入栈、压栈"""
        self.items.append(item)

    def put(self):
        """出栈"""
        return self.items.pop()


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.put())
    print(stack.put())
