def solution(participant, completion) -> str:
    freq = {}
    for player in participant:
        if player not in freq:
            freq[player] =1
        else :
            freq[player] +=1
    for player in completion:
        freq[player] -=1
    
    for key in freq : 
        if freq[key] == 1:
            return key
    


participant = ["aa","bb","cc","dd","aa"]
completion = ["aa","cc","dd","bb"]
print(solution(participant,completion))