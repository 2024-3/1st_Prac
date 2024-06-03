def solution(clothes):
    daily_look = {}
    
    # 각 종류별로 옷을 분류
    for value, key in clothes:
        if key in daily_look:
            daily_look[key].append(value)
        else:
            daily_look[key] = [value]
    
    # 각 종류별로 옷의 수 + 1(입지 않는 경우)
    count = 1
    for values in daily_look.values():
        count *= (len(values) + 1)
    
    # 아무것도 입지 않는 경우는 제외
    answer = count -1
    return answer


