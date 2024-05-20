def solution(phone_book):
    phone_book = sorted(phone_book)
    prefix_map = {}

    for number in phone_book:
        for i in range(1, len(number)):
            prefix = number[:i]
            if prefix in prefix_map:
                return False
        prefix_map[number] = True

    return True