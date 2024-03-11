import heapq

food_times = [3,1,1,1,2,4,3]
k = 12 #
# 정답 6
#풀이 참고: https://velog.io/@jungmiin/
#todo: 다시풀것.
def solution(food_times, k):

    #전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times)<=k:
        return -1

    q=[]
    # O(200,000)
    for i in range(len(food_times)):
        #(음식 시간, 음식 번호) 형태로 heapq에 삽입
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0 #먹기 위해 사용한 시간
    previous = 0 #직전에 다 먹은 음식 시간

    length = len(food_times) #남은 음식의 개수


    while sum_value+((q[0][0]-previous)*length)<=k:
        now=heapq.heappop(q)[0] #현재의 음식 시간
        sum_value += (now-previous)*length #음식시간이 이전과 같다면, 더해지지 않는다 (이전에 이미 빠졌으므로)
        length -= 1 #다 먹은 음식 제외
        previous = now #이전 음식 시간 재설정

    #남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x:x[1]) #음식의 번호 기준으로 정렬
    return result[(k-sum_value)%length][1]

print(solution(food_times, k))
