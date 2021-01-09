
def solution(s):
    answer = [0] * 500
    call =dict()
    for i in s.replace("{","").replace("}","").split(",") : 
        if i in call:
            call[i] +=1
        else : 
            call[i] = 1
    for j in call :
        answer[call[j]-1] = int(j)
    return answer[0:len(call)][::-1]
print(solution("{{123}}"))