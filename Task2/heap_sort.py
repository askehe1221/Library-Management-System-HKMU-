def heapify(arr, n, i, is_max_heap=True):
    """
    堆化过程
    :param arr: 待堆化的数组
    :param n: 数组长度
    :param i: 当前根节点索引
    :param is_max_heap: 是否为最大堆
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if is_max_heap:
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
    else:
        if left < n and arr[left] < arr[largest]:
            largest = left
        if right < n and arr[right] < arr[largest]:
            largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, is_max_heap)

def heapify_iterative(arr, n, i, is_max_heap=True):
    """
    非递归版本的堆化
    """
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if is_max_heap:
            if left < n and arr[left] > arr[largest]:
                largest = left
            if right < n and arr[right] > arr[largest]:
                largest = right
        else:
            if left < n and arr[left] < arr[largest]:
                largest = left
            if right < n and arr[right] < arr[largest]:
                largest = right
        
        if largest == i:
            break
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest

def heap_sort(arr, reverse=False, use_iterative=False):
    """
    堆排序
    :param arr: 待排序的数组
    :param reverse: 是否降序排序
    :param use_iterative: 是否使用迭代版本的堆化
    :return: 排序后的数组
    """
    if not arr:
        return []
    
    n = len(arr)
    heapify_func = heapify_iterative if use_iterative else heapify
    
    # 构建堆
    for i in range(n // 2 - 1, -1, -1):
        heapify_func(arr, n, i, not reverse)
    
    # 一个个取出元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify_func(arr, i, 0, not reverse)
    
    return arr

# 测试
print("=== 测试堆排序 ===")
# 测试0-based索引
test_arr1 = [10, 4, 15, 3, 6, 7]
print(f"原始数组: {test_arr1}")
print(f"升序排序: {heap_sort(test_arr1.copy())}")
print(f"降序排序: {heap_sort(test_arr1.copy(), reverse=True)}")
print(f"迭代版本: {heap_sort(test_arr1.copy(), use_iterative=True)}")