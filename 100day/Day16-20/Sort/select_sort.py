# @author: huhao
# @file: select_sort.py
# @time: 2019/7/25 8:05
# @Document：https://www.python.org/doc/
# @desc:
'''
for i=0 -> len(array)-1:
    min_index = i
    for j = i+1 -> len(array):
        if(array[min_index] > array[j])
            min_index = j
    swap(array[min_index], array[i])

'''

def select_sort(origin_items, comp=lambda x, y: x < y):
    '''简单选择排序'''
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]  # python中交换两列表元素方法
    return items


def main():
    items = [2, 1, 4, 3, 5, 3, 6, 7, 5]
    items_sorted = select_sort(items)
    print(items_sorted)


if __name__ == '__main__':
    main()