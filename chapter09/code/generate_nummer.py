def the_right_commend():

    while(True):
        num = input("请输入:")
        flag = False
        if len(num) <= 3:
            print("长度正确")
            set_nummer={"0","1","2","3","4","5","6","7","8","9"}
            set_num = set(num)
            if set_nummer.issuperset(set_num):
                print("数据正确")
                print(num)
                flag = True
            else:
                print("数据不正确，请重新输入")


        else:
            print("长度不正确 请重新输入")
        if flag == True:
            break
the_right_commend()