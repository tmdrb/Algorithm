# Algorithm
알고리즘 정리

## 완전탐색 알고리즘

모든 경우의 수를 다 체크해서 정답을 찾는 방법

완전탐색 알고리즘 적용 경우

1. 해결하고자 하는 문제의 가능한 경우의 수를 대략적으로 계산
2. 가능한 모든 방법을 다 고려
- Brute Force - 반복/조건문 활용해서 모든 경우 테스트
- 순열
- 재귀호출
- 비트마스크
- BFS,DFS

4. 실제 답을 구할 수 있는지 적용

### 순열 

### DFS (깊이우선탐색)

stack 자료구조 사용

1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리
   방문하지 않은 노드가 없으면 스택에서 최상단 노드를 꺼낸다
3. 2번을 수행 할 수 없을 때까지 반복

```
def DFS(graph ,v , visited):
    
    visited[v] = True
    print(v)
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            DFS(graph,i,visited)
```

### BFS (너비우선탐색)

queue 자료구조 사용

1. 탐색 시작 노드를 큐에 삽입
2. 큐에서 노드를 꺼낸 다음 해당 노드의 인접노드를 다시 큐에 삽입하고 방문 처리
3. 2번을 수행 할 수 없을 때까지 반복

```
def BFS(graph,v,visited):
    queue = list()
    queue.append(v)
    visited[v] = True
    
    while len(queue) != 0 : 
        head = queue[0]
        print(head , queue)
        if len(queue) > 1:
            queue = queue[1:]
        else:
            queue.pop()
   
        for i in graph[head]:
            if not visited[i] :
                queue.append(i)
                visited[i] = True
        
```

