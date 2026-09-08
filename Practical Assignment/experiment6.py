# Video Editing App - Matrix Chain Multiplication

# Video segments with render dimensions/costs
# Each pair represents the dimensions of an effect
segments = [
    ("Effect 1", 10, 20),
    ("Effect 2", 20, 30),
    ("Effect 3", 30, 40),
    ("Effect 4", 40, 30),
    ("Effect 5", 30, 20)
]

# Extract dimensions
dimensions = [segments[0][1]]

for segment in segments:
    dimensions.append(segment[2])

n = len(segments)

# DP table
dp = [[0] * n for _ in range(n)]

# Table to store optimal split positions
split = [[0] * n for _ in range(n)]

# Matrix Chain Multiplication
for length in range(2, n + 1):

    for i in range(n - length + 1):
        j = i + length - 1
        dp[i][j] = float('inf')

        for k in range(i, j):

            # Cost of merging two effects
            cost = (
                dp[i][k]
                + dp[k + 1][j]
                + dimensions[i]
                * dimensions[k + 1]
                * dimensions[j + 1]
            )

            if cost < dp[i][j]:
                dp[i][j] = cost
                split[i][j] = k


# Generate optimal parenthesization
def get_order(i, j):
    if i == j:
        return segments[i][0]

    k = split[i][j]

    left = get_order(i, k)
    right = get_order(k + 1, j)

    return "(" + left + " × " + right + ")"


# Display video segments
print("Video Segments:")
for name, rows, cols in segments:
    print(name, ":", rows, "x", cols)

print("\nMinimum Processing Time:", dp[0][n - 1])

print("\nOptimal Merging Order:")
print(get_order(0, n - 1))

# Display DP table
print("\nDP Table:")

for row in dp:
    print(row)