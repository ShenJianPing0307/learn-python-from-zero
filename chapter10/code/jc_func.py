def jc(n):
    """
    5! = 5 * 4 * 3 * 2 * 1
    jc(n) = n * jc(n-1)
    :param n:
    :return:
    """
    if n == 1:
        return 1
    else:
        return n * jc(n - 1)  # 3 * jc(2) --> 3 * 2 * jc(1) --> 3 * 2 * 1 * jc(0)


res = jc(5)  # 5 * 4 * 3 * 2 * 1 = 120
print(res)
