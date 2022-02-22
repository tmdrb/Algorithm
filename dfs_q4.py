"""
프로그래머스 dfs 단어 변환 문제

해결방법

1. 처음 문자에서 배열에 있는 단어 중 하나라도 변화는 단어확인
2. 1 진행 한다음 방문한 단어인지 체크
3. 위 과정을 반복
"""

def compare(b,e):
    
    temp = []
    
    for i in range(len(list(b))):
        if b[i] != e[i]:
            
            temp.append(b[i])
    
  
    if len(temp) == 1:
        return True
    
    return False
    

def dfs(begin,end,words,visited):
    global m,answer
    
    if ''.join(begin) == ''.join(end):
        
        m = min(m,answer)
    
    else:
        for n,word in enumerate(words):
            
            if not visited[n]:
                
                if compare(begin,word): 
                    
                    answer += 1
                    visited[n] = True
                    
                    dfs(list(word),end,words,visited)
                        
                    answer -= 1
                    visited[n] = False
            
                
                
                    
def solution(begin, target, words):
    global m,answer
    m = 100
    answer = 0
    visited = [False] * len(words)
    dfs(list(begin),list(target),words,visited)
    
    if m == 100:
        m = 0
    
    return m
