#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(food_times, k): #k: k초만큼 음식을 먹은 뒤 방송이 중단되기 시작
    #k가 food_times.length보다 크면, food_times의 1씩 빼는 연산을 처음 원소로 되돌아가 적용해야 한다. 따라서 for는 쓸 수 없다.
    time = 0
    while k >= 0:
        #k초에 먹어야 했던 음식의 위치를 반환해야 한다
        #current = food_times[time % len(food_times)]
        if k == 0:
            print((time % len(food_times)) + 1)
            break
            return 1
        #도중에 다 먹은 경우(값이 0인 경우)는 넘긴다
        if food_times[time % len(food_times)] == 0:
            time += 1 #그냥 continue하면 time 값이 변경되지 않은 채로 다음 루프를 돌기 때문에 루프가 끝나지 않는다
            continue
        else:
            #k초가 되기 전까지는 매 초마다 음식을 1초 분량씩 먹어야 한다
            food_times[time % len(food_times)] -= 1
            #print("K: " + str(k))
            k -= 1
        time += 1 #도중에 0이 있는 경우를 넘겨야 하는데, 이때 k는 줄어들면 안되지만(먹은 게 없으므로), 0이 아닌 음식으로 넘어가야 하므로 time은 항상 늘어나야 한다
        #for idx, food_time in enumerate(food_times):
        #    print(idx, food_time, time)

#solution([1,1], 1)
#solution([2,1], 2)

#noprob solution([2,1,2], 4)
#noprob solution([1,0,1], 1)

#solution([3,1,2], 5)
#solution([2,0,2], 3)
#solution([2,0,1], 2)
#food_tm, k, time
#[1,0,1], 1, 1
#[1,0,1], 1, 2
#[1,0,0], 0, 3
