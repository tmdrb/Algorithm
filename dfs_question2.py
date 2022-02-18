"""
늑대와 양 문제

전형적인 백트래킹 문제

dfs로 노드를 탐색해 가는데 조건에 맞는 탐색을 해 나간다.

현재 노드에서 양이 늑대보다 더 많으면 다음 노드로 이동

다음 노드로 이동 할 때 현재 노드를 지우고 다음 노드의 자식 노드를 추가해 나가는 방식
"""
def changegraph(edge,n):
    graph = [[] for i in range(n)]  
    for i,j in edge:
        graph[i].append(j)
        
    return graph
  
def dfs1(graph,info,v,child,sheep,wolf):
    
    
    global output
    
    output = max(output,sheep)
    if info[v] == 0:
        sheep += 1
    else:
        wolf += 1  
        
    for e in child:
        
      
        if sheep > wolf :
            
            child.remove(e)
            child += graph[e]
            
            dfs1(graph,info,e,child,sheep,wolf)
