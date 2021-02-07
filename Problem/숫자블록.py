
'''
    so_su = [begin]
    for i in range(begin+1,end+1) :
        test =0
        for j in so_su:
            if i % j == 0:
                test +=1
        if test == 0:
            so_su.append(i)
    so_su.reverse()
    print(so_su)
    answer = []

    
    return answer


print(solution(1, 100))
'''