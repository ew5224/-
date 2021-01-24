from operator import itemgetter

def solution(genres, plays): 
    tuple_list = []
    check_dict = {}
    for i in range(len(genres)) :
        tuple_list.append((genres[i],playes[i],i))
        if genres[i] in check_dict.keys():
            check_dict[genres[i]] += plays[i]
        else :
            check_dict[genres[i]] = plays[i]
    sort_list = sorted(check_dict, reverse=True)
    #tuple_list.sort(key=lambda i : i[0], reverse=True)
    tuple_list = sorted(tuple_list, key=itemgetter(0,1), reverse=True)
    print(tuple_list)
    answer = [x[2] for x in tuple_list]
    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
playes = [500, 600, 150, 800, 2500]

result = solution(genres, playes)
print(result)