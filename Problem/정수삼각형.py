# def solution(triangle):
#     height =len(triangle)
#     a = tri(triangle)
#     answer = a.down(triangle[0][0], level=0, position=0)
#     return answer

# class tri :
#     def __init__(self, triangle) :
#         self.dict={}
#         self.triangle =triangle

#     def down(self, result, level, position) :
#         if level+1 == len(self.triangle) :
#             return result
#         if (level, position) in self.dict.keys() :
#             return self.dict[(level, position)]
#         result = max(self.down(result + self.triangle[level+1][position], level+1, position), self.down(result+self.triangle[level+1][position+1], level+1,position+1))
#         self.dict[(level,position)] =result
#         print(self.dict)
#         return result
def solution(triangle):
    for i in range(1, len(triangle)) :
        level = len(triangle) -i
        new_tri = []
        for j in range(len(triangle) - i):
            new_tri.append(max(triangle[level][j] ,triangle[level][j+1]) +  triangle[level-1][j])
        triangle[level-1] = new_tri
    
    
    answer = triangle[0][0]



    return answer
triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))


