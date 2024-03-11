# limit = 100

# 70, 60, 55, 50, 45,  40
# start_point          dest_point

def solution(people, limit):
    dest_point = len(people)-1
    answer = 0
    people.sort(reverse = True)

    for i in range(len(people)):
        start_point = i
        if start_point > dest_point:
            break
        if start_point == dest_point:
            answer += 1
            continue
        if limit - people[start_point] >= people[dest_point]: # 100- 50 == 50 / 100-40 > 50 과 같은 경우.
            dest_point -= 1
        answer += 1
    return answer

# print(solution([70, 50, 80, 50], 100))
# print(solution([70, 80, 50], 100))