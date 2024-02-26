# 큰 수의 법칙

n, m, k = map(int, input().split())
ls = list(map(int, input().split()))

# m개, k개 중복 가능


ls.sort()
biggest = ls[-1]
second_biggest = ls[-2]

num_second_biggest = m // (k+1)
num_biggest = (m // (k+1)) * k + m % (k+1)


answer = num_biggest * biggest + num_second_biggest * second_biggest

print(answer)