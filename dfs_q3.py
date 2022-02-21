"""
여행 경로 문제

DFS로 접근 

모든 경로를 다 방문해야 하므로 방문해야 할 노드들을 따로 저장

방문해야 할 노드 리스트가 null이 되면 정답에 한개씩 추가

전체 정답 sort 해서 알파벳순서가 가장 빠른 정답 출력
"""

def makegraph(tickets):
    
    keys = set()
    for i,j in tickets:
        keys.add(i)
        keys.add(j)
        
    dic = dict()
    for i in keys:
        dic[i] = list()
    for key,value in tickets:
        dic[key].append(value)
    
    return dic
        
def ds(graph,v,child,route):
    global answer,n
    
    child.remove(v)
    route.append(v)
    
    if not child:
        
        if len(route) > n:
            answer.append(list(route))
    
    for i in graph[v]:
        if i in child:
            
            ds(graph,i,child,route)
            child.append(i)
            route.remove(i)
            
def solution(tickets):
    global answer,n
    answer = []
    route = []
    
    graph = makegraph(tickets)
    child = [j for i in list(graph.values()) for j in i]
    n = len(child)
    child.append("ICN")
    ds(graph,"ICN",child,route)
    
    if len(answer) > 1 :
        answer.sort()
    
    return answer[0]
