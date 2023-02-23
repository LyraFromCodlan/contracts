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
        row_upper = (friend_position+variants_num+1)//2
        column_upper = 1 if (friend_position+variants_num)%2 else 2
        row_lower = (friend_position-variants_num+1)//2
        column_lower = 1 if (friend_position-variants_num)%2 else 2
        if friend_position+variants_num<=students_num:
            if friend_row - row_lower < row_upper - friend_row:
                ofile.write(str(row_lower)+" "+str(column_lower)+"\n")
            else:
                ofile.write(str(row_upper)+" "+str(column_upper)+"\n")
        else:
            ofile.write(str(row_lower)+" "+str(column_lower)+"\n")