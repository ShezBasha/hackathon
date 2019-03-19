#bubble sorted
def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    for x in range(0, len(items)-1):
         for y in range(0, len(items)-1-x):
             if items[y] > items[y+1]:
                 items[y], items[y+1] = items[y+1], items[y]
    return items

#merge sort
def merge(first, last):
    new_list = []
    while len(first) > 0 and len(last) > 0:
        if first[0] < last[0]:
            new_list.append(first[0])
            first.pop(0)
        else:
            new_list.append(last[0])
            last.pop(0)

    if len(first) == 0:
        new_list = new_list + last
    if len(last) == 0:
        new_list = new_list + first

    return new_list


def merge_sort(items):

    '''Return array of items, sorted in ascending order'''

    len_i = len(items)
    if len_i == 1:
        return items

    mid_point = int(len_i / 2)
    x = merge_sort(items[:mid_point])
    y = merge_sort(items[mid_point:])

    return merge(x, y)

#quick sort
def quick_sort(items):

    '''Return array of items, sorted in ascending order'''

    xlen = len(items)

    if xlen <= 1:
          return items

    piv = items[0]
    lower = []
    higher = []
    mid = []
    for i in items:
        if i < piv:
            lower.append(i)
        elif i > piv:
            higher.append(i)
        elif i == piv:
            mid.append(i)

    lower = quick_sort(lower)
    higher = quick_sort(higher)

    return lower + mid + higher
