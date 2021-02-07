def solution(n):
    if n % 2 == 1 :
        return 0
    if n ==2 : 
        return 3
    if n==4 :
        return 11
    f2 = 3
    f4 = 11
    f_list = [0, f2,f4]
    for i in range(n//2 -2) : 
        f_list.append(2+2*sum(f_list) +f_list[-1])
    answer = f_list[-1]
    return answer %1000000007

print(solution(6))