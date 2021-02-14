def solution(clothes :list) -> int:
    cloth_dict = {}    
    for cloth in clothes :
        if cloth[1] in cloth_dict:
            cloth_dict[cloth] +=1
        else :
            cloth_dict[cloth[1]] = 1
    
    def caculate(case : list) -> int:
        answer =0
        count =0
        while count > len(case) :
            pass
        return 


    return caculate(cloth_dict.values())
    