from collections import Counter


def solution(clothes):
    clothes_orgr = Counter([clothing[1] for clothing in clothes])
    
    answer = 1 
    for c in clothes_orgr.values():
        answer *= (c+1)
        
    return answer-1