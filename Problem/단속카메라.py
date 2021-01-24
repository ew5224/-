

# def solution(routes):
#     check = dict()
#     for route in routes : 
#         for i in range(route[1] - route[0] + 1) :
#             if route[0] +i in check.keys() : 
#                 check[route[0] + i] +=1
#             else : 
#                 check[route[0] +i] =1
    
#     total_car = len(routes)
#     answer = 0
#     while total_car > 0: 
#         max_value = max(check.values())
#         max_key = [k for k, v in check.items() if v == max_value] 
        
#         remove_list = []
#         for route in routes :
#             if max_key[0] >= route[0] and max_key[0] <= route[1] :
#                 for i in range(route[1] - route[0] + 1) :
#                     check[route[0] + i] -=1
#                 total_car -=1
#                 remove_list.append(route)
#         for route in remove_list :
#             routes.remove(route)
        
#         answer +=1
#     return answer


routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
a = solution(routes)
print(a)


def solution(routes):
    routes.sort(key=lambda x:x[1])
    last = -30000 
    answer= 0
    for route in routes :
        if route[0] > last :
            answer +=1
            last = route[1]
    return answer
