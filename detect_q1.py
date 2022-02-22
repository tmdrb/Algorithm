"""
프로그래머스 완전탐색 배열안에 수들의 조합으로 소수 찾기 문제
안겹치게 하기 위해서 완전탐색으로 경우의 수들을 뽑아야한다.
dfs 이용해서 조합 뽑는다
소수 찾는 알고리즘으로 소수 찾는다. (제곱근을 구해서 for문 )
"""
import math

def find(n):
    if n < 2:
        return False
    elif n < 4:
        return True
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if n % i ==0 :
                return False
                
    return True
    
def comb(numbers,visited,n,child):
    
    global b
    
    for i in range(n):
        if not visited[i]:
            
            child += [numbers[i]]
            
            b.append(list(child))
            visited[i] = True
            comb(numbers,visited,n,child)
            visited[i] = False
            child.pop()

def change(b):
    numberlist =set()
    
    for i in b:
        su = 0
        n = len(i)
        for k,j in enumerate(i):
            su += int(math.pow(10,n-k-1)) * j
            
        numberlist.add(su)
            
        
        
    return numberlist    
        
        
def solution(numbers):
    global b
    
    b=[] 
    child =[]
    visited = [False] * len(numbers)
    answer = 0
    
    comb(numbers,visited,len(numbers),child)    
    
    numlist = change(b)
    print(numlist)
    for i in numlist:
        if find(i):
            print(i)
            answer+=1
    
    return answer
