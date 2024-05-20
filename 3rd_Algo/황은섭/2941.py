letter = ["c=", "c-", "dz=", "d-", "lj", "nj", "z=", "s="]
input_letter = str(input())
sum = 0

for word in letter:
  check = input_letter.count(word)            #count()메서드로 크로아티아 문자가 얼마나 있는지 확인
  if check:
    input_letter = input_letter.replace(word, ' ')# 해당하는 문자 지우기
    for i in range(check):                    #문자가 있는 수 만큼 sum에 추가
      sum += 1

input_letter = input_letter.replace(' ', '')  #공백 삭제
sum += len(input_letter)                      #총 문자 갯수 세기
print(sum)
