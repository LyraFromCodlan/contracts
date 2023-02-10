N = int(input())
country = []
salaries = [int(salary) for salary in input().split()][0:N]
degree = [int(salary) for salary in input().split()][0:N]
exclusive = [int(salary) for salary in input().split()][0:N]
for ind in range(0,N):
    country.append([salaries[ind], degree[ind], exclusive[ind]])
salaries.clear()
degree.clear()
exclusive.clear()
Q = int(input())
traitors = []
t_salaries = [int(salary) for salary in input().split()][0:Q]
t_degree = [int(salary) for salary in input().split()][0:Q]
t_exclusive = [int(salary) for salary in input().split()][0:Q]
for ind in range(0,Q):
    flag = True
    for c_ind in range(0,N):
        if (t_exclusive[ind] == c_ind+1 and country[c_ind][2]==1) or (t_salaries[ind] >= country[c_ind][0] and t_degree[ind] >= country[c_ind][1]):
            print(c_ind+1,end=" ")
            flag = False
            break
    if flag:
        print(0, end=" ")