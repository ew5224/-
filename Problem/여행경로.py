def solution(tickets):
    answer = []
    for ticket in tickets :
        if ticket[0] == "ICN":
            answer.append(solver(tickets.remove(ticket), 1, len(tickets), ["ICN"]))
    print(answer)
    return answer

def solver(tickets, num, final_num, visit) :
    if num == final_num :
        return visit
    

    for ticket in tickets: 
        if ticket[0] == visit[-1]:
            return solver(tickets.remove(ticket), num+1, final_num, visit.append(ticket[1]))
    return "a"
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

    
print (solution(tickets))