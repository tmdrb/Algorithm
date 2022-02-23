"""
heap 자료구조

완전 이진트리로 최소,최댓값을 빠르게 찾아낼 수 있는 자료구조

우선순위 큐 로 활용

최대 힙 -> 항상 부모노드가 자식노드(root *2, root*2+1)보다 커야한다.

insert -> 마지막에 값 삽입후 순차적으로 부모노드와 비교해 나가면서 교환
delete -> 루트노드 삭제후 마지막 노드 값을 root로 설정 한 뒤 힙 구성
"""

def delete(heap):
    heap[1] = heap[-1]
    heap = heap[:-1]
    
    root = 1
    v = len(heap) -1
    
    while root*2+1 <= v and (heap[root] <= heap[root *2] or heap[root] <= heap[root *2 +1]):
        
        temp = heap[root]
        
        if heap[root *2] >= heap[root*2+1]:
            heap[root] = heap[root *2]
            heap[root *2] = temp
            root *= 2
        else:
            heap[root] = heap[root *2+1]
            heap[root *2+1] = temp
            
            root = root*2 +1
    
    return heap
    
def insert(heap,n):
    heap.append(n)
    v = len(heap)-1
    
    while (heap[v//2] < heap[v]) :
        
        temp = heap[v//2]
        heap[v//2] = heap[v]
        heap[v] = temp
        v = v//2
        
    return heap
