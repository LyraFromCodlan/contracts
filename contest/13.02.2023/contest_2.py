# import string

# with open("contest_2_test_1.txt","r") as ifile:
#     k = int(ifile.readline())
#     line = ifile.readline().strip()
#     max=1+k
    
#     letters={char:[] for char in string.ascii_lowercase}
#     for ind in range(len(line)):
#         letters[line[ind]].append(ind)
#     for char in letters:
#         # print(char+": ",end=' ')
#         # print(letters[char])
#         for ind in range(0,len(letters[char])):
#             counter = 1
#             limit = k
#             if len(letters[char])>1:
#                 # print("ind: "+str(ind))
#                 index = ind+1
#                 while index<len(letters[char]) and limit - letters[char][index] + letters[char][index-1] + 1 >=0:
#                     distance = letters[char][index] - letters[char][index-1] - 1
#                     # print("limit: "+str(limit))
#                     # print("distance: "+str(distance)+"; "+str(letters[char][index]))
#                     limit = limit - distance
#                     counter+=distance+1
#                     # print("counter: "+str(counter))
#                     index+=1
#                 if max<counter:
#                     max=counter+limit
# print(max)

import string

with open("'input.txt'","r") as ifile:
    k = int(ifile.readline())
    line = ifile.readline().strip()
    max=1+k if len(line) > k else len(line)

    for ind in range(0,len(line)-1):
        counter = 1
        limit = k
        if len(line)>1:
            index = ind+1
            last_char_ind = index
            while index<len(line) and limit>0:
                if line[index] == line[ind] and limit - index + last_char_ind + 1>=0:
                    distance = index - last_char_ind - 1
                    limit = limit - distance
                    counter+=distance+1
                index+=1
        if max<counter:
            max=counter+limit


print(max)