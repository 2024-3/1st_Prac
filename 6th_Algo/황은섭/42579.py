
def solution(genres, plays):
    
    counts = {} # 총 플레이 횟수를 저장하는 dict
    
    for key, value in zip(genres, plays):
        if key in counts:
            counts[key].append(value)
            counts[key] = [sum(counts[key])]
        else:
            counts[key] = [value]
    
    #재생 횟수 높은 장르부터 출력
    counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse = True)) #revers = True -> 내림차순
    keys = counts.keys()
    
    answer = []
    
    #장르, 고유번호에 맞게 list만들기
    for key in keys:
        
        answer_key = {}
        #genres에서 원하는 장르의 인덱스들을 저장
        answer_key = {index: plays[index] for index, value in enumerate(genres) if value == key}
        
        #딕셔너리에서 value 값을 내림차순으로한 고유번호 얻기
        sorted_key = sorted(answer_key, key=answer_key.get, reverse=True)
        
        answer += sorted_key[:2]

    return answer
