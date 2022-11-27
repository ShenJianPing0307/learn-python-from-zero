admin_list = ["admin1", "admin2", "admin3"]


def is_permission(func):
    def inner(instance, *args, **kwargs):
        if not hasattr(instance, "name"):
            if instance in admin_list:
                func()
        elif instance.name in admin_list:
            func()
        else:
            print("无权限进行操作！")

    return inner


class Student:
    """学生信息"""

    def __init__(self, name, addr, *args, **kwargs):
        self.name = name
        self.addr = addr

# 中间件 处理很多函数都要带装饰器的问题
class System:
    """对学生的各种操作"""

    def __init__(self):
        self.stu = []

    @is_permission
    def add_student(self, student):
        self.stu.append(student)

    @is_permission
    def del_student(self, name):
        for student in self.stu:
            if student.name == name:
                self.stu.remove(student)


def main():
    system = System()
    while (True):
        print("学生管理系统".center(30, "*"))
        print("1.添加学生信息")
        print("2.删除学生信息")
        print("3.修改学生信息")
        print("4.查询学生信息")
        print("5.显示所有学生信息")
        print("6.退出系统")
        print("*".center(35, "*"))
        num = input("请您输入正确序号:")
        if num == "1":
            # 新建学生
            stu = Student(input("请输入姓名:"), input("请输入地址:"))
            # 保存学生
            system.add_student(stu)
            print("添加成功")


main()
