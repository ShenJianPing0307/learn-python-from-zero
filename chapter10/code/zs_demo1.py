# 登陆检查
# 拥有权限的管理员
admin_info = [{"id": 1012, "username": "superadmin01", "password": "123456"},
              {"id": 1013, "username": "superadmin02", "password": "123456"},
              ]

# 一旦登陆成功，保存登陆的人的信息
login_user = {"username": "superadmin03", "password": "123456"}


def check_login(func):
    def inner(*args, **kwargs):
        for user in admin_info:
            if login_user.get("username") == user.get("username") and login_user.get("password") == user.get(
                    "password"):
                func()
                break
            else:
                print("非管理员，无权限操作！")
                break

    return inner


@check_login
def add_student():
    """增加学生的代码逻辑"""
    print("增加学生成功！")


@check_login
def del_student():
    pass


add_student()
del_student()
