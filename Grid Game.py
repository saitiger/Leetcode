class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        first_row_remain_sum = sum(grid[0])  
        second_row_remain_sum = 0
        minimized_robot2_sum = float('inf')

        for robot1_col in range(len(grid[0])):  
            first_row_remain_sum -= grid[0][robot1_col]

            best_of_robot2 = max(first_row_remain_sum, second_row_remain_sum)
            minimized_robot2_sum = min(minimized_robot2_sum, best_of_robot2)

            second_row_remain_sum += grid[1][robot1_col]

        return minimized_robot2_sum
