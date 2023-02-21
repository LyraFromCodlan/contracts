import string

alphabet = {letter: 0 for letter in string.ascii_lowercase}

with open("input.txt","r") as ifile:
    k = int(ifile.readline())
    line = ifile.readline().strip()
    length = len(line)

    for letter in alphabet:
        pointer_1 = 0
        limit = k
        for pointer_2 in range(0,length):
            if line[pointer_2]!=letter:
                limit -= 1
            if limit<0:
                if pointer_2-pointer_1>alphabet[letter]: alphabet[letter] = pointer_2 - pointer_1
                pointer_1+=1
                while line[pointer_1]!=alphabet[letter]:
                    pointer_1+=1
                limit+=1
    #     limit = k
    #     temp_ind=ind+1
    #     while temp_ind<length-1:
    #         if line[temp_ind]!=line[ind]:
    #             limit-=1
    #         if limit<0:
    #             break
    #         temp_ind+=1
    #     if max<temp_ind-ind+1:
    #         max = temp_ind-ind  
    # print(max)


# with open("input.txt","r") as ifile:
#     k = int(ifile.readline())
#     line = ifile.readline().strip()
#     length = len(line)
#     max=1

#     for ind in range(0,length):
#         limit = k
#         temp_ind=ind+1
#         while temp_ind<length-1:
#             if line[temp_ind]!=line[ind]:
#                 limit-=1
#             if limit<0:
#                 break
#             temp_ind+=1
#         if max<temp_ind-ind+1:
#             max = temp_ind-ind  
#     print(max)