def quick_sort(l_data:list, low:int, high:int) -> None:
    #如果不只有一个元素：
    if low < high:
        data_t = l_data[low]
        i = low
        j = high
        while i < j:
            #从后向前
            #两者中必须有一个包含“=”，否则会陷入死循环
            while i < j and l_data[j] >= data_t:
                j -= 1
            l_data[i] = l_data[j]

            #从前向后
            while i < j and l_data[i] < data_t:
                i += 1
            l_data[j] = l_data[i]
        l_data[i] = data_t
        quick_sort(l_data, low, i-1)
        quick_sort(l_data, i+1, high)

    else:
        return

if __name__ == "__main__":
    x = [5,4,6,3,7,8,4,9]
    print("排序前：", x)
    quick_sort(x,0,len(x)-1)
    print("排序后：", x)