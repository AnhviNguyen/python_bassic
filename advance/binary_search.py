def binary_search(list, element):
    start =0
    end = len(list)
    middle =0
    step =0

    while (start <= end):
        #cat lat: list[start : end+1] la lay ngay o vi tri dau tien, thuong thi khong lay end ma chi lay phan tu dung truoc end, neu end+1 thi lay luon phan tu ati vi tri end do
        print("Step ", step, " : ", list[start:end+1])
        step +=1

        middle = (start +end) //2

        if list[middle] == element:
            return middle
        elif list[middle] < element:
            start = middle +1
        else:
            end = middle -1
        
    return -1

list = [1,2,3,4,5,6,7,8]
target = 8

binary_search(list, target)

