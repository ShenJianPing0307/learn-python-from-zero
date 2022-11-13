# 函数重试机制 微服务

def retry(tries):
    def wrapper(func):
        def inner(*args, **kwargs):
            for _ in range(tries):
                func(*args, **kwargs)

        return inner

    return wrapper


@retry(tries=5)  # @wrapper
def get_goods_price():
    print("执行成功！")
    pass


get_goods_price()
