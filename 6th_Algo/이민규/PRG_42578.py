def solution(clothes):
    clothes_dict = {}
    for index in input:   
        if index in clothes_dict:
            clothes_dict[index[1]] += 1
        else:
            clothes_dict[index[1]] = 1

    case = 1
    for key in clothes_dict:
        case = case * (clothes_dict[key] + 1)
        
    return case - 1
