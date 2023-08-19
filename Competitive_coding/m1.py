def overall_distortion(N, issue_counts):
    overall_distortion_value = 0
    prev = sum(issue_counts[0])

    for hour in range(1, N):
        curr = sum(issue_counts[hour])
        if curr>prev:
            overall_distortion_value += (curr - prev)
        prev = curr
    return overall_distortion_value

# Read the number of working hours (N) from input
N = int(input())

# Read the issue counts for each hour and server
issue_counts = []
for _ in range(N):
    counts = list(map(int, input().split()))
    issue_counts.append(counts)

# Calculate the overall distortion for the day
overall_distortion_value = overall_distortion(N, issue_counts)

# Print the overall distortion value
print(overall_distortion_value)


# 5
# 1 3 4 1 3
# 3 5 1 9 7
# 1 1 1 2 0
# 4 3 1 7 9
# 32 1 4 6 8