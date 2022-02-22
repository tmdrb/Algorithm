"""
프로그래머스 dfs 네트워크 문제

1. 기존은 두개의 선이 존재하지만 하나의 선을 가진 그래프로 변경
2. 처음 노드부터 끝까지 탐색
3. 방문노드를 체크해가면서 dfs가 끝나면 answer +1
"""
def makegraph(computers):
    graph = []
    
    
    for n,i in enumerate(computers):
        temp = []
        for k,element in enumerate(i):
            if n != k and element == 1:
                temp.append(k)
        graph.append(temp)

    return graph

def dfs(graph,v):
    global visited
    
    visited[v] = True
    
    for c in graph[v]:
        
        if not visited[c]:
            
            dfs(graph,c)
            
        
        
    
def solution(n, computers):
    global visited
    
    visited = [False]*n
    answer = 0
    graph = makegraph(computers)
    
    for i in range(n):
        if not visited[i]:
            dfs(graph,i)
            answer+=1
            
    
    return answer
