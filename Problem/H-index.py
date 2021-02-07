def solution(citations):
    citations.sort()
    max_len = len(citations)
    done = False
    level = max_len
    while not done and level >0:
        if citations[max_len -level] >= level:
            done = True
        else : 
            level -=1
    answer = level
    return answer