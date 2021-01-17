def solution(n):
    divider =3
    left =n % 9

    n = n // 9
    answer = 0
    m = 100
    while  n != 0:
        answer +=(n % 3) * m
        print(answer)
        m *= 10
        n = n // 3
    if left != 0:
        answer += ((left-1) // 3) * 10 + ((left-1) % 3) + 1
    answer = str(answer).replace("3","4")    
    return answer

print(solution(42)) 