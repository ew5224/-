def solution(skill, skill_trees):
    answer = 0
    for q in skill_trees :
        find =0
        find2=0
        while(find < len(skill) and find2 < len(q)):
            if q[find2] == skill[find]:
                find +=1
                find2 +=1
            else :
                find2 +=1
        if find == len(skill)-1:
            answer +=1

    return answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))