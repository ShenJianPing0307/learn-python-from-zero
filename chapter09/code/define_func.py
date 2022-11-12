
def login(username, password):
    # 从数据库中取出注册时的用户信息
    user_name = "zs"
    pass_word = "123456"
    # 前台传递的用户信息和存储的信息进行比对
    if user_name == username and pass_word == password:
        return "验证通过"
    else:
        return "验证失败"

def login1(username, password):
    # 从数据库中取出注册时的用户信息
    user_name = "zs"
    pass_word = "123456"
    # 前台传递的用户信息和存储的信息进行比对
    msg = "验证失败"
    if user_name == username and pass_word == password:
        msg = "验证通过"
    return msg

res = login1("zs", "123456")
print(res)