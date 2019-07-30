# @author: huhao
# @file: bubble_sort.py
# @time: 2019/7/25 8:27
# @Document：https://www.python.org/doc/
# @desc:
'''
for i=0 -> len(array)-1:
    for j=len(array)-1 -> i+1:
        if(array[j]>array[j+1])
            swap(array[j], array[j+1]))

'''


def bubble_sort(origin_items, comp=lambda x, y: x > y):
    '''高质量冒泡排序（搅拌排序）
        双向冒泡排序，一端是从小到大排序，另一端是从大到小排序
    '''
    items = origin_items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j+1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j-1],items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


def main():
    items = [2, 1, 4, 3, 5, 3, 6, 7, 5]
    item2 = ["apple","banana","pitaya","watermelon","cat"]
    items_sorted = bubble_sort(item2)
    print(items_sorted)


if __name__ == '__main__':
    main()