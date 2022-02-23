"""
프로그래머스 N으로 표현

N을 1개 가지고 ~ N을 8개 가지고 까지 dp에 저장

여기에 값이 없으면 -1 있으면 숫자 반환

집합별로 사칙연산
"""
def solution(N,number):
    
    final_dp = [[] for i in range(9)]
    
    for i in range(1,9):
        temp = set()
        if i == 1:
            final_dp[1]+=[N]
        else:
            temp.add(int(str(N)*i))
            for j in range(1,int(i/2 + 0.5)):
                
                for s1 in final_dp[j]:
                    for s2 in final_dp[i-j]:
                        
                        temp.add(s1+s2)
                        temp.add(s1*s2)
                        if s2 != 0 and s1%s2 ==0:
                            temp.add(int(s1/s2))
                        
                        temp.add(s1-s2)
                        
                for s1 in final_dp[i-j]:
                    for s2 in final_dp[j]:
                        if s2 != 0 and s1%s2 ==0:
                            temp.add(int(s1/s2))
                        temp.add(s1-s2)
                
                
            if i % 2 == 0:
                j = int(i/2)
                
                for s1 in final_dp[j]:
                    for s2 in final_dp[j]:
                        
                        temp.add(s1+s2)
                        temp.add(s1*s2)
                        if s2 != 0 and s1%s2 ==0:
                            temp.add(int(s1/s2))
                        temp.add(s1-s2)
            
        if number in temp:
            return i
        
        final_dp[i] += list(temp)            
                
    return -1       
