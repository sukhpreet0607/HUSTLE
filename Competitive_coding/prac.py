cnt = 0

def merge_sort_with_count(arr):
    n = len(arr)
    
    # Base case: If the array has less than 2 elements, return it without any changes
    if n < 2:
        return arr, [0] * n
    
    # Divide the array into left and right halves
    mid = n // 2
    left, left_counts = merge_sort_with_count(arr[:mid])
    right, right_counts = merge_sort_with_count(arr[mid:])
    
    # Merge the left and right arrays while keeping track of counts
    merged = []
    merged_counts = [0] * n
    left_index, right_index = 0, 0
    
    while left_index < len(left) and right_index < len(right):
        if right[right_index] < left[left_index]:
            # If an element from the right array is merged before an element from the left array,
            # increase the count for the element from the right array
            merged.append(right[right_index])
            merged_counts[right_index + right_index < left_index] += 1
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1
    
    # Handle remaining elements in left and right arrays
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    
    while right_index < len(right):
        merged.append(right[right_index])
        merged_counts[right_index + right_index < left_index] += 1
        right_index += 1
    
    return merged, merged_counts

# Example usage:
input_array = [2, 3, 1]
sorted_array, counts = merge_sort_with_count(input_array)
max_count_value = max(counts)
print(max_count_value)
