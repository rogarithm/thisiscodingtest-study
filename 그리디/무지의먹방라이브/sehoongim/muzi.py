#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    sub_1_all = k / len(food_times)
    sub_1_first_x = k % len(food_times)
    food_times = [v - sub_1_all for v in food_times]

    #food_times의 길이보다 작은 k의 나머지값만큼 0이 아닌 요소에서 1씩 뺀다
    x = sub_1_first_x
    i = 0
    while x > 0:
        if food_times[i] == 0:
            i += 1
            continue
        if food_times[i] != 0:
            food_times[i] -= 1
            i += 1
            x -= 1

    i = 0
    while i < len(food_times):
        if food_times[i] <= 0:
            i += 1
            continue
        elif food_times[i] != 0:
            print(i + 1)
            return i + 1
        i += 1
    print(-1)
    return -1 #i >= len(food_times)이면 모든 요소가 0이라는 뜻. 그러니 더 먹을 음식이 없다
