"""
도둑이 빈집을 터는 경우 최대 금액 구하기

동적프로그래밍 알고리즘으로 접근

원으로 첫번째 집과 마지막 집이 붙어있어 까다로움

1. 첫번째 집을 털고 마지막 집을 안털은 경우
2. 첫번째 집을 안털고 마지막 집을 턴 경우

이렇게 두고 동적프로그래밍 적용

집 하나하나의 경우를 생각하면 복잡해짐

발상의 전환 문제
"""

def solution(money):
    answer = 0
    
    n = len(money)
    dp = [0] * n
    
    for i in range(0,n-1):
        if i == 0 and i == 1:
            dp[i] = money[i]
      
        else:
            dp[i] = max(money[i]+dp[i-2],dp[i-1])
            
    
    for i in range(1,n):
        if i == 1 and i == 2:
            dp[i] = money[i]
      
        else:
            dp[i] = max(money[i]+dp[i-2],dp[i-1])
            
    answer = dp[-1]
    return answer
