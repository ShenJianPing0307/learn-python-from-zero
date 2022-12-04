"""
将脚本与修改的文件放在一起
"""
import os

"""
{"1.xlsx":"cw01.xls",...}
"""
BASE_DIR = os.path.dirname(os.path.abspath(__name__)) # 如果出现路径找不到问题，就是用os.path.realpath
path_rename_file = os.path.join(BASE_DIR, "rename_file.txt")

name_dict = {}


def get_name_map():
    with open(path_rename_file) as f:
        for line in f:
            yield line


for line in get_name_map():
    origin_name, modified_name = line.strip().split(",")
    name_dict[origin_name] = modified_name

files_list = os.listdir()

for file in files_list:
    try:
        src = os.path.join(BASE_DIR, file)
        dst = os.path.join(BASE_DIR, name_dict[file])
        os.rename(src, dst)
    except KeyError:
        continue

# 如果多个目录，下面多个文件，怎么办？
# os.walk()

