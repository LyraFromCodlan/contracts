import operator

with open("input.txt","r") as ifile, open("output.txt","w") as ofile:
    students_num = int(ifile.readline().strip())
    variants_num = int(ifile.readline().strip())
    friend_row = int(ifile.readline().strip())
    friend_column = int(ifile.readline().strip())

    friend_position = ((friend_row-1)*2+friend_column)
    friend_variant = friend_position%variants_num if friend_position%variants_num!=0 else variants_num
    if students_num < variants_num+friend_variant:
        ofile.write("-1\n")
    else:
        op = operator.add if friend_position+variants_num<=students_num and friend_row - (friend_position-variants_num+1)//2 >= (friend_position+variants_num+1)//2 - friend_row else operator.sub
        row = op(friend_position+1,variants_num)//2
        column = 1 if op(friend_position,variants_num)%2 else 2
        ofile.write(str(row)+" "+str(column)+"\n")