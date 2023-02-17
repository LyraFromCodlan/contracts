with open("input.txt","r") as ifile:
    degree_of_beauty : int = 0
    letters_nums=list()
    n = int(ifile.readline())
    for i in range(0,n):
        letters_nums.append(int(ifile.readline()))
    # print(letters_nums)

    def count_recursive(array: list) -> int:
        if len(array) == 1 or array==[]:
            return 0
        elif len(array) == 2:
            if 0 in array:
                 return 0
        elif array[0] == 0:
            array.remove(0)
        elif array[-1]==0:
            array=array[:-1]
        
        temp_degree_of_beauty = min(array) * (len(array)-1)
        minimum = min(array)
        nulls_list = [0]
        arrays_list = list()
        for ind in range(0,len(array)):
            array[ind]-=minimum
            if array[ind] == 0:
                nulls_list.append(ind)
        nulls_list.append(len(array)-1)
        # print("null list: "+str(nulls_list))
        for ind in range(1,len(nulls_list)):
            arrays_list.append(array[nulls_list[ind-1]+1:nulls_list[ind]+1])
            # print("array list: "+str(array[nulls_list[ind-1]+1:nulls_list[ind]+1]))
        for arr in arrays_list:
            temp_degree_of_beauty += count_recursive(arr)

        return temp_degree_of_beauty

    print(count_recursive(letters_nums))