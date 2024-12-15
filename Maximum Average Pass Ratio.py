# On each pass add extra student to each list the then the list which has the highest difference before and after (Gain) is selected. 
# Need to do this at all stages since adding +2 to one list at one go does not guarantee increase so need to do +1 at each step and calculate gain.
class Solution:
    def maxAverageRatio(
        self, classes: List[List[int]], extraStudents: int
    ) -> float:
        def calculate_gain(passes, total_students):
            return (passes + 1) / (total_students + 1) - passes / total_students

        max_heap = []
        for passes, total_students in classes:
            gain = calculate_gain(passes, total_students)
            heapq.heappush(max_heap, (-gain, passes, total_students))

        for _ in range(extraStudents):
            current_gain, passes, total_students = heapq.heappop(max_heap)
            heapq.heappush(
                max_heap,
                (
                    -calculate_gain(passes + 1, total_students + 1),
                    passes + 1,
                    total_students + 1,
                ),
            )
        total_pass_ratio = 0
        while max_heap:
            _, passes, total_students = heapq.heappop(max_heap)
            total_pass_ratio += passes / total_students
        return total_pass_ratio / len(classes)
