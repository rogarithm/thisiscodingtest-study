class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sorted_people = sorted(people, key = lambda person: (-person[0], person[1]))
        answer = []
        for person in sorted_people:
            answer.insert(person[1], person)
        return answer

print(Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))