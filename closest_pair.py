import sys
def printClosest(array1, array2, g, h, m):
    difference=sys.maxsize
    l = 0
    v = h-1
    while(l < h and v >= 0):
        if abs(array1[l] + array2[v] - m) < difference:
            res_l = l
            res_v = v
            difference = abs(array1[l] + array2[v] - m)
        if array1[l] + array2[v] > m:
            v=v-1
        else:
            l=l+1
            print("The closest pair is [", array1[res_l],",",array2[res_v],"]")
array1 = [6, 40, 50, 70]
array2 = [15, 22, 35, 45]
g = len(array1)
h = len(array2)
m = 38
printClosest(array1, array2, g, h, m)
