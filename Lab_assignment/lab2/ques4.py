def max_activities_with_array(activities):
    # Sort activities based on their finishing times
    activities.sort(key=lambda x: x[1])
    
    count = 0
    prev_finish_time = float('-inf')
    selected_activities = []
    
    # Iterate through the sorted activities
    for activity in activities:
        start_time, finish_time = activity
        # If the current activity can be performed after the previous one finishes
        if start_time >= prev_finish_time:
            count += 1
            selected_activities.append(activity)
            prev_finish_time = finish_time
    
    return count, selected_activities

# Example:
activities = [(1, 3), (2, 5), (3, 8), (4, 6), (5, 9), (7, 10)]
max_count, max_activities_array = max_activities_with_array(activities)
print("Maximum number of activities performed:", max_count)
print("Activities array with maximum number of activities:", max_activities_array)
