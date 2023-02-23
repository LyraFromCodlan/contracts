with open("input.txt","r") as ifile, open("output.txt","w") as ofile:
    n = int(ifile.readline().strip())
    coordinates = [int(coordinate) for coordinate in ifile.readline().strip().split()]
    x_min = coordinates[0]
    x_max = coordinates[0]
    y_min = coordinates[1]
    y_max = coordinates[1]
    for ind in range(0,n-1):
        coordinates = [int(coordinate) for coordinate in ifile.readline().strip().split()]
        x_min = coordinates[0] if coordinates[0] < x_min else x_min
        x_max = coordinates[0] if coordinates[0] > x_max else x_max
        y_min = coordinates[1] if coordinates[1] < y_min else y_min
        y_max = coordinates[1] if coordinates[1] > y_max else y_max

    ofile.write(str(x_min)+" "+str(y_min)+" "+str(x_max)+" "+str(y_max)+"\n")