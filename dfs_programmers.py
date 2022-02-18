def makegraph(tickets):
    
    keys = set()
    for i,j in tickets:
        keys.add(i)
        keys.add(j)
        
    dic = dict()
    for i in keys:
        dic[i] = set()
    for key,value in tickets:
        dic[key].add(value)
        
           
        
    return dic
        
def bfs(graph,v):
    global answer
    
    answer.append(v)
    li = list(graph[v])
    
    for i in li:
        li.remove(i)
        graph[v] = set(li)
       
        bfs(graph,i)
    
def solution(tickets):
    global answer
    answer = []
   
    
    graph = makegraph(tickets)
    
    bfs(graph,"ICN")
    print(answer)
    return answer
