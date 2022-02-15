"""
아이스크림 나누기 문제
같은 0 끼리는 붙어있고 1은 떨어져 있다고 가정
붙어있는 0은 하나로 취급
2차 배열에서 0끼리 붙어있는 개수 찾는 문제

문제해결 방법
1. 완전탐색으로 접근
2. 상하좌우를 dfs로 탐색 0인지 아닌지 확인
3. 2번을 행렬이 끝날 때 까지 이 과정에서 dfs가 끝나는걸 한덩어리로 취급해서 계산
"""

def dfs(graph,x,y,visited):
    
    if x >= 0 and x <= len(graph[0])-1 and y >= 0 and y <=len(graph)-1 :
        
        if graph[y][x] == 0 and not visited[y][x]:
            visited[y][x] = True
            
            dfs(graph,x-1,y,visited)
           
            dfs(graph,x+1,y,visited)
            
            dfs(graph,x,y-1,visited)
           
            dfs(graph,x,y+1,visited)
            
            return True
        else:
            return False
            
    else:
        return False
        
g = [[0,0,1],[0,1,0],[1,0,1]]
visited = [[False]*3 for i in range(3)]
result = 0      
        
for i in range(len(g)):
    for j in range(len(g[0])):
        if dfs(g,j,i,visited):
            result +=1
        
