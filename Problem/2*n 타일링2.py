def solution(n):
    a1 =1
    a2 =2
    for i in range(n-2):
        new = a1 + a2
        a1 =a2
        a2= new 
    return a2 % 1000000007

print(solution(100))