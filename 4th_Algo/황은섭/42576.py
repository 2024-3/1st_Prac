from collections import Counter

def solution(participant, completion):

    counter_p = Counter(participant)
    counter_c = Counter(completion)

    counter_result = counter_p - counter_c
    answer = list(counter_result.keys())

    return answer[0]