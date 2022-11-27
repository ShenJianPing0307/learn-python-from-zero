
def is_permission(func):
    def inner(student, *args, **kwargs):
        print(student)
        # if name in admin_list:
        #     func()
        # print("无权限进行操作！")

    return inner

@is_permission
def add_student(student):
    pass


add_student("abc")