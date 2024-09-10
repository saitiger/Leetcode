class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        end_time = logs[0][1]
        
        max_time_spent = end_time
        
        ans = {max_time_spent: [logs[0][0]]}
        
        for i in range(1, len(logs)):
            time_spent = logs[i][1] - end_time
            
            if time_spent == max_time_spent:
                ans[time_spent].append(logs[i][0])
            
            elif time_spent > max_time_spent:
                ans[time_spent] = [logs[i][0]]
                max_time_spent = time_spent
            
            end_time = logs[i][1]
        
        return min(ans[max_time_spent])

# Solution 2 - Without Hashmap
        max_time = 0
        employee_id = n

        prev_leave_time = 0
        for log in logs:
            curr_id, leave_time = log
            task_duration = leave_time - prev_leave_time
        
            if task_duration > max_time:
                max_time = task_duration
                employee_id = curr_id
            elif task_duration == max_time:
                employee_id = min(employee_id, curr_id)
        
            prev_leave_time = leave_time
    
        return employee_id
