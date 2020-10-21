def merge_sort(array):
    result = []
    if len(array) < 2:
        return array
    mid = int(len(array)/2)
    y = merge_sort(array[:mid])
    z = merge_sort(array[mid:])
    while (len(y) > 0) or (len(z) > 0):
        if len(y) > 0 and len(z) > 0:
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(z) > 0:
            for i in z:
                result.append(i)
                z.pop(0)
        else:
            for i in y:
                result.append(i)
                y.pop(0)
    return result
print(merge_sort([1,3,5,7,8,5,3,1,0]))
