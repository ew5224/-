def solution(n):
    answer= 0
    b = solver(n)
    for i in range(n //2 + 1):
        num1= n % 2 + 2*i
        num2 = n//2 - i
        answer+= (b.factorial(num1+num2) / b.factorial(num1)) / b.factorial(num2) 
    return int(answer% 1000000007)

class solver :
    def __init__(self,n):
        self.matrix = [1]*(n+1)
        iter = 1
        for i in range(1,n+1):
            iter = iter *i
            self.matrix[i] = iter
        

    def factorial(self, n1) :
        return self.matrix[n1]


print(solution(3))
