# @author: huhao
# @file: merge_sort.py
# @time: 2019/7/26 8:03
# @Document：https://www.python.org/doc/
# @desc:


def merge_sort(items, comp=lambda x, y: x <= y):
    '''归并排序（分治法）'''
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    return merge(left, right, comp)

def merge(items1, items2,comp):
    '''合并，将两个有序列表合并成一个有序列表'''
    items = []
    index1, index2 = 0, 0
    while index1