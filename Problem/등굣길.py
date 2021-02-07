def solution(m, n, puddles):
    answer = recur(1,1,m,n,puddles)
    return answer % 1000000007

def recur(x,y,m,n, puddles) :
    if [x,y] in puddles :
        return 0
    if x == m and y == n : 
        return 1
    elif x==m :
        return recur(x,y+1, m,n, puddles)
    elif y ==n :
        return recur(x+1, y, m,n, puddles)
    else : 
        return recur(x+1, y, m,n, puddles) + recur(x,y+1, m,n, puddles)


m, n =4,3
puddles= [[2,2]]
print(solution(m,n,puddles))