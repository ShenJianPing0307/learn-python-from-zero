log_text = "192.168.111.23 访问了你的网站,查看了你的主页,在2022-11-12日访问的"


def handle_log(seg, *args, **kwargs):
    if args:
        seg = args[0]
    msg = log_text.split(seg)
    print(msg)


# 后期需要变化以 - 进行分隔
handle_log(",", "-")
