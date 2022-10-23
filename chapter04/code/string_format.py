from string import Template

template = Template("$a-$a")
res = template.substitute(a="hello world")
print(res)
