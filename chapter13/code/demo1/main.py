"""
将脚本与修改的文件放在一起
"""
import os

"""
{"1.xlsx":"cw01.xls",...}
"""
BASE_DIR = os.path.dirname(os.path.abspath(__name__))  # 如果出现路径找不到问题，就是用os.path.realpath
path_rename_file = os.path.join(BASE_DIR, "file", "rename_file.txt")

name_dict = {}


def get_name_map():
    with open(path_rename_file) as f:
        for line in f:
            yield line


for line in get_name_map():
    origin_name, modified_name = line.strip().split(",")
    name_dict[origin_name] = modified_name

for root, dirs, files in os.walk(os.path.join(BASE_DIR, "file")):

    for file in files:
        try:
            src = os.path.join(root, file)
            dst = os.path.join(root, name_dict[file])
            os.rename(src, dst)
        except KeyError:
            continue
