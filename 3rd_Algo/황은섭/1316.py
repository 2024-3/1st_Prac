num = int(input())
words = []
sum = 0

for n in range(num):
    word = input().strip()
    words.append(word)

for word in words:
    word = str(word)
    # 3. 문자를 훑어보면서. 그 문자의 갯수를 센다.
    # 3.
    for i in range(len(word)):
        count = word.count(word[i])
        first = word.find(word[i])
        final = word.rfind(word[i])

        if i == (len(word) - 1):
            sum += 1
        elif count == 1:
            continue
        elif (final - first) != (count - 1):  # 맨 마지막 놈 인덱스 - 첫 놈 인덱스 = 문자갯수 -1
            break  # 위의 식 만족 못하면 탈락

print(sum)
