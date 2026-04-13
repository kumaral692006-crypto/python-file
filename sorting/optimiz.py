def bubble_sort_optimization(arr):
    n=len(arr)

    for i in range(n):
        swapped=False
        for j in range(0,n-1):
            if arr[j]>arr[j+1]:
                arr[j].arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr

arr=[1,2,3,4,5]
print("optimized sorted",bubble_sort_optimization(arr))