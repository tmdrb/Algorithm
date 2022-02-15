""" 카카오 2022 q4
양궁 점수 문제
해결 방법:
완전 탐색으로 해결 -> 하나하나 for문으로 살펴보기에는 가짓수가 너무 많아서 DFS를 이용
dfs를 사용하는데 조건을 설정
1. 처음 쏜 애보다 무조건 +1 을 하거나 0 으로 해서 dfs를 돌려서 가짓수를 낮춘다.
2. 다른 경우에서 최댓값이 나올수 있으므로 1번 조건을 만족하지 않더라도 마지막에 남은 화살 개수로 경우의수 확인

""" 
global max_val,answer
answer = [0] *11
max_val = 0

def listsum(original,new_list):
    original_sum_val = 0
    new_sum_val = 0
    for i in range(11):
        if original[i] > new_list[i] :
            original_sum_val += 10 - i
        if original[i] < new_list[i] :
            new_sum_val += 10 - i
            
    return new_sum_val - original_sum_val


def DFS(scores,k,v,temp):
    global max_val,answer
    
    if v < 11:
        
        if v == 10 :
            
            if k == 0:
                temp[v] = 0
                
                sum_val = listsum(scores,temp)
                if max_val < sum_val :
                    max_val = sum_val
                    answer = temp[:]
                   
                    
            else :
                if k - (scores[v] +1) == 0:
                    
                    temp[v] = scores[v]+1
                    sum_val = listsum(scores,temp)
                    if max_val < sum_val :
                        max_val = sum_val
                        answer = temp[:]
                else:
                    temp[v] = k
                    sum_val = listsum(scores,temp)
                    if max_val < sum_val :
                        max_val = sum_val
                        answer = temp[:]
                
                    
        else:
            temp[v] = 0
            DFS(scores,k,v+1,temp)
            
            if k >= scores[v] +1:
                temp[v] = scores[v]+1
                DFS(scores,k-(scores[v] +1),v+1,temp)
                
    
       
            
graph = [0,0,1,2,0,1,1,1,1,1,1]
visited = [False]*11
temp =  [0]*11
