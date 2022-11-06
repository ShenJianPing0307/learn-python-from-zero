data = [
    {"id":1, "pid":None, "title": "文档"},
    {"id":2, "pid":None, "title": "引导页"},
    {"id":3, "pid":None, "title": "权限测试页"},
    {"id":4, "pid": None, "title": "组件"},
    {"id":5, "pid":3, "title": "页面权限"},
    {"id":6, "pid":3, "title": "指令权限"},
    {"id":7, "pid":3, "title": "角色权限"},
    {"id":8, "pid":4, "title": "富文本编辑器"},
    {"id":9, "pid":4, "title": "Markdown"},
]
# print(data[2]["title"])
# print("---", data[4]["title"])
#
# ll = [{"权限测试页":[{},{}]},{"组件":[{},{}]}]




""" 输出：
文档
引导页
权限测试页
--- 页面权限
--- 指令权限
--- 角色权限
组件
--- 富文本编辑器
--- Markdown
"""