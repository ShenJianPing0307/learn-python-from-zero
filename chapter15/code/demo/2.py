import time
from threading import Thread


def merge(li, start, mid, last):
    """
    :param li: 传入的序列
    :param start: 序列第一个位置的索引
    :param mid: 序列中间位置的索引
    :param last: 序列最后一个元素的索引
    :return:
    """
    i = start  # 左边开始指针的位置
    j = mid + 1  # 右边开始指针的位置

    temp = []  # 申请临时空间
    while i <= mid and j <= last:  # 当两个指针都没有移动到序列尾部
        if li[i] < li[j]:
            temp.append(li[i])
            i += 1
        else:
            temp.append(li[j])
            j += 1
    while i <= mid:  # 当右边的指针移动到尾部，将左侧的剩下元素全部拷贝到temp
        temp.append(li[i])
        i += 1
    while j <= last:  # 当左边的指针移动到尾部，将右侧的剩下元素全部拷贝到temp
        temp.append(li[j])
        j += 1

    li[start:last + 1] = temp  # 将临时列表中的元素再赋给li列表，节约空间


def cal_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__}", end_time - start_time)
    return inner


def mergeSort1(li, start, last):
    if start < last:  # 至少两个元素，一个元素是有序的
        mid = (start + last) // 2  # 取整
        mergeSort1(li, start, mid)  # 对左侧元素进行分解，当进行分解到一个元素时，不满足 start<last，退出递归函数，执行 merge(li,start,mid,last)，就会将左侧排序好
        mergeSort1(li, mid + 1, last)
        merge(li, start, mid, last)

def mergeSort2(li, start, last):
    if start < last:  # 至少两个元素，一个元素是有序的
        mid = (start + last) // 2  # 取整
        t1 = Thread(target=mergeSort2, args=(li, start, mid))
        t2 = Thread(target=mergeSort2, args=(li, mid + 1, last))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        # mergeSort(li,start,mid) #对左侧元素进行分解，当进行分解到一个元素时，不满足 start<last，退出递归函数，执行 merge(li,start,mid,last)，就会将左侧排序好
        # mergeSort(li,mid+1,last)
        merge(li, start, mid, last)


import random


li = [i for i in range(10000)]
random.shuffle(li)

mergeSort1(li, 0, len(li) - 1)
print("mergeSort1",li)
mergeSort2(li, 0, len(li) - 1)
print("mergeSort2",li)  # [0, 1, 2, 5, 6, 8, 9]

