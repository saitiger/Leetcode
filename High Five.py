# Brute Force 
def average_of_top_five_brute_force(items):
    student_scores = defaultdict(list)
    for student_id, score in items:
        student_scores[student_id].append(score)
    result = []
    for student_id in sorted(student_scores.keys()):
        scores = sorted(student_scores[student_id], reverse=True)
        top_five = scores[:5]
        average = sum(top_five) // 5  
        result.append([student_id, average])
    return result

# Using Heap 
def average_of_top_five(items):
    student_scores = defaultdict(list)
    for student_id, score in items:
        heapq.heappush(student_scores[student_id], score)
        if len(student_scores[student_id]) > 5:
            heapq.heappop(student_scores[student_id])  
    result = []
    for student_id in sorted(student_scores.keys()):
        top_five_scores = student_scores[student_id]
        avg_score = sum(top_five_scores) // 5 
        result.append([student_id, avg_score])
    return result
