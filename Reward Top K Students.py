class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:

        # Creating set of negative and positive feedback for o(1) lookup
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)

        students = [] # Heap for finding top k students 
        for s_id, rep in zip(student_id, report):
            score = sum((3 if word in positive_feedback else -1 for word in rep.split() if word in positive_feedback or word in negative_feedback))
            if len(students) == k:
                heapq.heappushpop(students, (score, -s_id)) # Using student id to break the tie 
            else:
                heappush(students, (score, -s_id))
        
        return [-heappop(students)[1] for _ in range(k)][::-1]
