# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-04-22 14:33
# IDE: PyCharm
# =========================================================

def bubbleSort(arr):
    '''冒泡法
    （1）算法步骤
比较相邻的元素。如果第一个比第二个大，就交换他们两个。
对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
针对所有的元素重复以上的步骤，除了最后一个。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
O(n^2)'''
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selectionSort_1(arr):
    n = len(arr)
    if n == None or n == 1: return arr
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def selectionSort(nums):
    '''选择排序：
    （1）算法步骤
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
重复第二步，直到所有元素均排序完毕。'''
    n = len(arr)
    if n == None or n == 1: return arr
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

def insertionSort(arr):
    '''插入排序：
    将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）'''
    n = len(arr)
    if n == None or n == 1: return arr
    for i in range(len(arr)):
        preIndex = i-1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex-=1
        arr[preIndex+1] = current
    return arr

def shellSort(arr):
    '''引入分治的思想，对插入排序进行改良'''
    import math
    gap=1
    while(gap < len(arr)/3):
        gap = gap*3+1
    while gap > 0:
        for i in range(gap,len(arr)):
            temp = arr[i]
            j = i-gap
            while j >=0 and arr[j] > temp:
                arr[j+gap]=arr[j]
                j-=gap
            arr[j+gap] = temp
        gap = math.floor(gap/3)
    return arr

def mergeSort(arr):
    import math
    if (len(arr) < 2):
        return arr
    middle = math.floor(len(arr) / 2)
    left, right = arr[0:middle], arr[middle:]


    def merge(left,right):
        result = []
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        while left:
            result.append(left.pop(0))
        while right:
            result.append(right.pop(0))
        return result

    return merge(mergeSort(left), mergeSort(right))

def quickSort(arr, left=None, right=None):

    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]


    def partition(arr, left, right):
        pivot = left
        index = pivot+1
        i = index
        while  i <= right:
            if arr[i] < arr[pivot]:
                swap(arr, i, index)
                index+=1
            i+=1
        swap(arr,pivot,index-1)
        return index-1

    left = 0 if not isinstance(left,(int, float)) else left
    right = len(arr)-1 if not isinstance(right,(int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
    return arr

def countingSort(arr, maxValue):
    '''基数排序'''
    bucketLen = maxValue+1
    bucket = [0]*bucketLen
    sortedIndex =0
    for i in range(len(arr)):
        if not bucket[arr[i]]:
            bucket[arr[i]]=0
        bucket[arr[i]]+=1
    for j in range(bucketLen):
        while bucket[j]>0:
            arr[sortedIndex] = j
            sortedIndex+=1
            bucket[j]-=1
    return arr

def bucket_sort(s):
    """桶排序"""
    import math
    min_num = min(s)
    max_num = max(s)
    # 桶的大小
    bucket_range = math.ceil((max_num-min_num)/ len(s))
    # 桶数组
    count_list = [ [] for i in range(len(s) + 1)]
    # 向桶数组填数
    for i in s:
        count_list[int((i-min_num)//bucket_range)].append(i)
    s.clear()
    # 回填，这里桶内部排序直接调用了sorted
    for i in count_list:
        for j in sorted(i):
            s.append(j)

def RadixSort(list):
    i = 0                                    #初始为个位排序
    n = 1                                     #最小的位数置为1（包含0）
    max_num = max(list) #得到带排序数组中最大数
    while max_num > 10**n: #得到最大数是几位数
        n += 1
    while i < n:
        bucket = {} #用字典构建桶
        for x in range(10):
            bucket.setdefault(x, []) #将每个桶置空
        for x in list: #对每一位进行排序
            radix =int((x / (10**i)) % 10) #得到每位的基数
            bucket[radix].append(x) #将对应的数组元素加入到相 #应位基数的桶中
        j = 0
        for k in range(10):
            if len(bucket[k]) != 0: #若桶不为空
                for y in bucket[k]: #将该桶中每个元素
                    list[j] = y #放回到数组中
                    j += 1
        i += 1
    return  list

arr = [5,15,14,6,15,22,76,34,13,25,6]
# arr = mergeSort(arr)
arr = RadixSort(arr)
print(arr)
