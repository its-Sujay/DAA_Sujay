def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Sort the intervals based on their start times
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:  # If the current interval overlaps with the last interval in merged list
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))  # Merge the intervals
        else:
            merged.append(interval)
    
    return merged

# Example :
intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
merged_intervals = merge_intervals(intervals)
print("Non-overlapping intervals after merging:", merged_intervals)
def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Sort the intervals based on their start times
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:  # If the current interval overlaps with the last interval in merged list
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))  # Merge the intervals
        else:
            merged.append(interval)
    
    return merged

# Example usage:
intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
merged_intervals = merge_intervals(intervals)
print("Non-overlapping intervals after merging:", merged_intervals)
