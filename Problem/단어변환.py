def solution(begin, target, words):
    if target not in words :
        return 0
    answer = solver(begin, target, words, 0) 
    if not (answer < 50) : 
        return 0
    return answer

def solver(begin, target, words,num) :
    if begin == target : 
        return num
    length = len(begin)
    result_list = []
    for word in words :
        a = 0
        b= words
        b.remove(word)
        for i in range(length):
            a += int(begin[i] == word[i])
        if a == length-1 : 
            print(word)
            result_list.append(solver(word, target, b, num +1))
    return min(result_list)
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))