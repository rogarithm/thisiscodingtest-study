word = input().rstrip()
tag_on = False
answer = ''
word_stack = []

#.join 과 += 의 차이
for i in word:
    if i == '<':  #tag_on == False
        tag_on = True
        while word_stack:
            answer += word_stack.pop()
        # join 되는지 확인 필요
        answer += i
        continue
    if i == '>': #tag_on == True
        tag_on = False
        answer += i
        continue
    if i == ' ':
        while word_stack:
            answer += word_stack.pop()
        answer += i
        continue
    #tag_on & i!='>'
    elif tag_on:
        answer += i
        continue
    #tag_on! & i!= 태그/빈칸 아닌 그냥 문자.
    else:
        word_stack.append(i)

# 마지막이 단어로 끝난다면, 남은 스택을 털어줘야 한다.
while word_stack:
    answer += word_stack.pop()

print(answer)

