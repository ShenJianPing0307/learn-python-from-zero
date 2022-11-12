data = [
    {"id":1, "pid":None, "title": "文档"},
    {"id":2, "pid":None, "title": "引导页"},
    {"id":3, "pid":None, "title": "权限测试页"},
    {"id":4, "pid": None, "title": "组件"},
    {"id":5, "pid":3, "title": "页面权限"},
    {"id":6, "pid":3, "title": "指令权限"},
    {"id":7, "pid":3, "title": "角色权限"},
    {"id":8, "pid":4, "title": "富文本编辑器"},
    {"id":9, "pid":4, "title": "Markdown"}
] # 数量不知道
"""
  {
   3: {"id":3, "pid":None, "title": "权限测试页",
      children:[{"id":5, "pid":3, "title": "页面权限"},{"id":6, "pid":3, "title": "指令权限"}]
       },
   4: {"id":4, "pid": None, "title": "组件", 
   children:[{"id":8, "pid":4, "title": "富文本编辑器"},]
      },
    1:{"id":1, "pid":None, "title": "文档",children:[]},
    }
"""

def get_parent_child_relation():
    menu_dict = {}
    for item in data:
        menu_id = item["id"]
        menu_pid = item["pid"]
        menu_title = item["title"]
        if not menu_pid:
            menu_dict[menu_id] = {
                "id":menu_id,
                "pid":menu_pid,
                "title":menu_title,
                "children":[]
            }
        else:
            menu_dict[menu_pid]["children"].append(item)

    menu_list = menu_dict.values()
    print(menu_list)

    for item in menu_list:
        print(item["title"])
        children = item.get("children")
        if children:
            for item1 in children:
                print("---", item1["title"])


get_parent_child_relation()
# l_father=[]
# l_son=[]
# for i in data:
#     if i.get("pid")==None:
#         l_father.append(i)
#     else:
#         l_son.append(i)
# for i in l_father:
#     print(i.get("title"))
#     for x in l_son:
#         if x.get("pid")== i.get("id"):
#             print("   "+ x.get("title"))



