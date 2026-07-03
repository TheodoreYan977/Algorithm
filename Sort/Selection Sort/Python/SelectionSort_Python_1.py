def Selection_Sort(arr):    #首先定义一个函数Selection_Sort，参数为一个数组arr
    n = len(arr)     #获取数组arr的长度n
    for i in range(n-1):     #外层循环，遍历数组arr的前n-1个元素
        min_idx = i      #假设当前元素为最小元素
        # 内层循环，从当前元素的下一个元素开始遍历数组arr的剩余元素
        # 如果发现更小的元素，更新min_idx
        for j in range(i + 1, n):    #内层循环，遍历数组arr的剩余元素
            if arr[j] < arr[min_idx]:    #如果当前元素arr[j]小于假设的最小元素arr[min_idx]
                min_idx = j    #更新min_idx为当前元素的索引
        arr[i], arr[min_idx] = arr[min_idx], arr[i]    #交换当前元素和最小元素
        print(f"第{i+1}轮排序后数组状态: {arr}")    #打印当前轮排序后的数组状态
    return arr   #返回排序后的数组arr

# 测试
arr = [2, 6, 7, 1, 3, 8, 9, 4, 10, 5]
print("排序前数组:", arr)
selection_sort(arr)
print("排序后数组:", arr)
