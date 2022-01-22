

N = int(input())
P = list(input().split())
C = list(input().split())

print(N)
print(P)
print(C)

def rev(days, P_lst, C_lst):
    revenue = 0
    fruit_cnt = 0
    curr_cost = 100
    for i in range(days):
        fruit_cnt += int(P_lst[i])
        if curr_cost <= 0:
            break
        elif int(C_lst[i]) <= fruit_cnt:
            fruit_cnt -= int(C_lst[i])
            revenue += (int(C_lst[i]) * curr_cost)
            curr_cost = 100 # cost 초기화
        else:
            curr_cost -= 20
    return f"{revenue / days:.2f}"

print(rev(N, P, C))
