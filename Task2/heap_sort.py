def heapify(arr,n,i):
    #把以i为根的子树调整为最大堆
    largest=i  #初始化最大堆
    left=2*i
    right=2*i+1
    # 左孩子大于根
    if left <= n and arr[left]>arr[largest]:
        largest=left
    #右孩子大于根
    if right <= n and arr[right]>arr[largest]:
        largest=right
    #最大不是i 交换并递归调整
    if largest != i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)



def heap_sort(arr):
    n=len(arr)-1#有效长度为1到end
    #建堆
    for i in range(n//2,0,-1):
        heapify(arr,n,i)
    #一个个取堆顶
    for i in range(n,1,-1):
        arr[1],arr[i]=arr[i],arr[1]
        heapify(arr,i-1,1)
    return arr
#测试
a=[None,10,4,15,3,6,7]
print(heap_sort(a))
