"""
student (name age gender)
"""
ll_name = ["zhangsan", "lisi"]
ll_age = [20, 21]
ll_gender = ["male", "male"]

print("姓名：%s, 性别：%s, 年龄：%s" % (ll_name[0], ll_gender[0], ll_age[0]))

"""
上面的方式，资源的消耗更大
"""
student1 = {"name": "zhangsan", "gender": "male", "age": 20}
student2 = {"name": "lisi", "gender": "male", "age": 21}

student_list = [student1, student2]
print("第一个学生 姓名：%s, 性别：%s, 年龄：%s" % (student_list[0]["name"],student_list[0]["gender"],student_list[0]["age"]))
print(student_list[0])
