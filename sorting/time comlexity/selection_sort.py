def selected_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=1
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr      
arr=[64,25,12,23,11]
sorted_arr=selected_sort(arr)
print("sorted array:",sorted_arr)
