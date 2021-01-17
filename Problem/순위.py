def solution(n, results):
    dict_win = dict()
    dict_lose = dict()
    for i in range(n+1):
        dict_win[i] = []
        dict_lose[i] = []
        
    for result in results:
        dict_win[result[0]].append(result[1])
        dict_lose[result[1]].append(result[0])
        check(dict_win, dict_lose, result[0], result[1])
        
    print(dict_win, dict_lose)

    answer =0
    for i in range(n+1):
        if len(list(set(dict_win[i]))) + len(list(set(dict_lose[i]))) == n-1:
            answer+=1
    
    return answer


def check(dict_win, dict_lose, win, lose):
    if lose not in dict_win[win]:
        dict_win[win].append(lose)
    if win not in dict_lose[lose] :
        dict_lose[lose].append(win)
    for i in dict_win[lose] :
        check(dict_win, dict_lose, win, i)
    for j in dict_lose[win] :
        check(dict_win, dict_lose, j, lose)

print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
