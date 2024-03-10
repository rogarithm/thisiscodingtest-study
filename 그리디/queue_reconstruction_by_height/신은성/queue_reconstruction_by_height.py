class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # k는 앞에 있는 사람 중에 h보다 크거나 같은 사람의 수

        ## 가장 큰 값으로 정렬 후, k위치에 삽입
        queue = []

        people.sort(key = lambda x : (-x[0], x[1]))

        for height, num_taller in people:
            queue.insert(num_taller, [height, num_taller])

        return queue

