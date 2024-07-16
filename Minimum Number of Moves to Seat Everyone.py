class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        moves = 0

        for i in range(len(seats)):
            moves+= abs(students[i] - seats[i])
        return moves

      # COUNT SORT 
        max_idx = max(max(seats), max(students))
        diff = [0] * (max_position)
        for location in seats:
            diff[location - 1] += 1
        for location in students:
            diff[location - 1] -= 1
        moves = 0
        unmatched = 0
        for difference in diff:
            moves += abs(unmatched)
            unmatched += difference
        return moves
