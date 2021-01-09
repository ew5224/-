def solution(N, number):
    a = solver(N)
    answer= a.solve(N, number,3)
    return answer




class solver:
    def __init__(self, N):
        self.matrix= [[],[N], [N, N+N, N*N, N//N, 11*N], [], [], [], [], [], []]

    def solve (self, N, number,iter):
        if N == number : 
            return 1
        if number in self.matrix[2]:
            return 2
        for i in range(1, iter):
            for j in self.matrix[i] :
                for k in self.matrix[iter-i] : 
                    if j + k == number :
                        return iter
                    else :
                        self.matrix[iter].append(j+k)
                        
                    if j- k == number :
                        return iter
                    
                    else : 
                        self.matrix[iter].append(j-k)
                    
                    if k- j == number :
                        return iter
                    
                    else : 
                        self.matrix[iter].append(k-j)

                    if j // k == number  :
                        return iter
                    
                    else : 
                        self.matrix[iter].append(j // k)

                    if k //j == number :
                        return iter
                    
                    else : 
                        self.matrix[iter].append(k // j)

                    if j * k == number :
                        return iter
                    
                    else : 
                        self.matrix[iter].append(j * k)
    
        newnum = 0
        for i in range(iter) :
            newnum += N * (10 ** i)

        if newnum == number:
            return iter
        else : 
            self.matrix[iter].append(newnum)

        self.matrix[iter] = list(set(self.matrix[iter]))
        self.matrix[iter].remove(0)
        
        if iter == 8 :
            return -1

        return self.solve( N, number, iter+1)




                  