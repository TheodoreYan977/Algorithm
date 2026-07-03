def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"第{i+1}轮排序后数组状态: {arr}")
    return arr

# 测试
arr = [2, 6, 7, 1, 3, 8, 9, 4, 10, 5]
print("排序前数组:", arr)
selection_sort(arr)
print("排序后数组:", arr)
