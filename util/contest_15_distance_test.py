import time

with open("input.txt","r") as ifile, open("output.txt","w") as ofile:
    towns = [int(van) for van in ifile.readline().strip().split()]
    
    # TEST FOR COMPLEXITY IN EXACT ALGORYTHM

    distances : list = []
    max_disatance : int = 0
    sum_distance : int = 0
    for town_ind in range(0,len(towns)):
        if towns[town_ind]-town_ind>max_disatance:
            max_disatance=towns[town_ind]-town_ind
        distances.append(str(towns[town_ind]-town_ind))
        sum_distance = sum_distance + towns[town_ind] - town_ind if towns[town_ind]-town_ind > 0 else sum_distance-towns[town_ind]+town_ind
    ofile.write(' '.join(sorted(distances)))
    print("max distance: %d" % max_disatance)
    print("sum of disnaces: %d" % sum_distance)

    # TEST FOR TIME COMPLEXITIES
    # CASE 1
    start_time_1 = time.time()
    original_list_1 = [el for el in range(100000)]
    for ind in range(100000):
        i = 0
        for ind_2 in range(100):
            if True:
                i+=1
    end_time_1=time.time()
    # print(end_time_1-start_time_1)
    print("CASE 1: %f" % float(end_time_1-start_time_1))
    
    #CASE 2
    start_time_2 = time.time()
    original_list_2 = [el for el in range(100000)]
    for ind in range(100000):
        i = 0
        generated_list = original_list_2[ind:]
        for ind_2 in range(16):
            if True:
                i+=1
    end_time_2=time.time()
    # print(end_time_2-start_time_2)
    print("CASE 2: %f" % float(end_time_2-start_time_2))
    
    # CASE 3
    start_time_3 = time.time()
    original_list_3 = [el for el in range(100000)]
    for ind in range(100000):
        i = 0
        generated_list = original_list_3[ind:]
        for ind_2 in range(21):
            if True:
                i+=1
    end_time_3=time.time()
    # print(end_time_3-start_time_3)
    print("CASE 3: %f" % float(end_time_3-start_time_3))
    