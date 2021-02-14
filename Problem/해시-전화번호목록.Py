def solution(phone_book : list) -> bool: 
    f
    answer = True
    return answer

def solution(phone_book): 
    for i in range(len(phone_book)): 
        pivot = phone_book[i] 
        for j in range(i+1, len(phone_book)): 
            strlen = min(len(pivot), 
            len(phone_book[j])) 
            if pivot[:strlen] == phone_book[j][:strlen]: 
                return False 
    
    return True