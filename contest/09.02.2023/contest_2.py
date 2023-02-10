n = int(input())
log = dict()
for ind in range(0,n):
    day, hour, minute, rocketId, event = map(str,[el for el in input().split()])
    time = int(day) *24*60 + int(hour)*60+int(minute)
    if rocketId not in log:
        log[rocketId] = 0
    if event == 'A':
        log[rocketId] = log[rocketId] - time
    elif event == 'C' or event == 'S':
        log[rocketId] = log[rocketId] + time

for el in sorted(list(log.values())):
    print(el,end=' ')