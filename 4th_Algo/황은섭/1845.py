def solution(poketmon):
    N = len(poketmon) // 2
    poketmon = set(poketmon)
    if N > len(poketmon):
        answer = len(poketmon)
    else:
        answer = N
    return answer