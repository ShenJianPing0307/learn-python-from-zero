l_dict_student = []
l_nummer = []
l_name = []
l_address = []

while(True):
    print("学生管理系统".center(30,"*"))
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.查询学生信息")
    print("5.显示所有学生信息")
    print("6.退出系统")
    print("*".center(35,"*"))
    num = input("请您输入正确序号:")
    # l_dict_student=[]
    # l_nummer=[]
    # l_name=[]
    # l_address=[]
    if num == "1":
        dict_student={}
        while(True):
            nummer = input("请输入学号")
            if not nummer in l_nummer:
                break
            else:
                print("学号已存在，请重新输入")
        l_nummer.append(nummer)
        dict_student["nummer"]=nummer
        dict_student["name"]=input("请输入姓名:")
        dict_student["address"]=input("请输入地址:")
        print(dict_student)
        l_dict_student.append(dict_student)
        print("添加成功")
    elif num == "2":
        while(True):
            flag = False
            nummer = input("请输入您要删除学生的学号:")
            for i in l_dict_student:
                if nummer == i.get("nummer"):
                    print(i)
                    print("这是您要删除的学生吗 yes/no")
                    x = input()
                    if x == "yes":
                        l_dict_student.remove(i)
                        flag = True
                        print("删除成功")
                    elif x == "no":
                        flag = True
                    else:
                        print("指令无法识别")
                        flag = True
                else:
                    print("查无此人，请重新输入学号")
            if flag == True:
                break
    elif num == "3":
        while(True):
            flag = False
            nummer = input("请输入您要修改学生的学号:")
            for i in l_dict_student:
                if nummer == i.get("nummer"):
                    print(i)
                    print("这是您要修改的学生吗")
                    while(True):
                        s = input("请输入您的选择yes/no:")
                        if s == "yes":
                            i["nummer"]=input("请输入新的学号:")
                            i["name"]=input("请输入新的名字:")
                            i["address"]=input("请输入新的地址:")
                            print("修改成功")
                            flag = True
                            break
                        elif s == "no":
                            break
                        else:
                            print("您输入的指令无法识别，请重新输入")

                else:
                    print("查无此人，请重新输入")
            if flag == True:
                break

    elif num == "4":
        print("请输入您要查询学生的学号:")
        nummer = input()
        for i in l_dict_student:
            if nummer == i.get("nummer"):
                print(i)
            else:
                print("查无此人")

    elif num == "5":
        for i in l_dict_student:
            print(i)

    elif num == "6":
        print("谢谢使用")
        break
    else:
        print("您输入的指令无法识别")

