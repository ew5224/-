# import heapq
# def solution(jobs):
#     heap = []
    
#     for job in jobs:
#         heapq.heappush(heap,(job[1]- job[0], job[0]))
#     heapq.heappop(heap)
#     return heap

# result = solution([[0, 3], [1, 9], [2, 6]])
# print(result)