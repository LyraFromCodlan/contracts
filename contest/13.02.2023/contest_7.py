with open("input.txt") as ifile:
    client_start = [int(el) for el in ifile.readline().split(':')]
    server_time = [int(el) for el in ifile.readline().split(':')]
    client_end = [int(el) for el in ifile.readline().split(':')]

    if client_start[0]>client_end[0]:
        client_end[0] = client_end[0] + 24

    client_start = (client_start[0]*3600 if client_start[0] else 0) + (client_start[1]*60 if client_start[1] else 0) + client_start[2]
    server_time = (server_time[0]*3600 if server_time[0] else 0) + (server_time[1]*60 if server_time[1] else 0) + server_time[2]
    client_end = (client_end[0]*3600 if client_end[0] else 0) + (client_end[1]*60 if client_end[1] else 0) + client_end[2]
    
    client_time_dif : float = client_end - client_start
    half_time = client_time_dif//2+1 if client_time_dif/2-client_time_dif//2>=0.5 else client_time_dif//2
    
    server_time = server_time+half_time

    hour = (server_time//3600)
    minute = (server_time - hour*3600)//60
    second = server_time - hour*3600 - minute *60

    hour = hour if hour<24 else hour - 24
    print((str(hour) if len(str(hour))>1 else '0'+str(hour)) +":"+(str(minute)if len(str(minute))>1 else '0'+str(minute))+":"+(str(second)if len(str(second))>1 else '0'+str(second)))