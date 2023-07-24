def sort(x_array, y_array):
    l = len(x_array)
    if l == 1:
        return x_array, y_array
    sorted_array_left, y_array_left = sort(x_array[:l // 2], y_array[:l // 2])
    sorted_array_right, y_array_right = sort(x_array[l // 2:], y_array[l // 2:])
    sorted_array = []
    sorted_array_y = []
    q_left = 0
    q_right = 0
    for step in range(l):
        left_index = min(len(sorted_array_left) - 1, q_left)
        right_index = min(len(sorted_array_right) - 1, q_right)
        if sorted_array_left[left_index] < sorted_array_right[right_index]:
            sorted_array.append(sorted_array_left[left_index])
            sorted_array_y.append(y_array_left[left_index])
            sorted_array_left[left_index] = 10 ** 8 + 1
            q_left += 1
        else:
            sorted_array.append(sorted_array_right[right_index])
            sorted_array_y.append(y_array_right[right_index])
            sorted_array_right[right_index] = 10 ** 8 + 1
            q_right += 1
    return sorted_array, sorted_array_y


def distance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def closest_pair(X, Y, X_prime, Y_prime, x_min=None, y_min=None):
    length = len(X) // 2
    if 2 == len(X):
        return distance([X[0], Y[0]], [X[1], Y[1]]), [X[0], Y[0]], [X[1], Y[1]]
    if 3 == len(X):
        d1 = distance([X[0], Y[0]], [X[1], Y[1]])
        d2 = distance([X[0], Y[0]], [X[2], Y[2]])
        d3 = distance([X[2], Y[2]], [X[1], Y[1]])
        if d1 <= d2 and d1 <= d3:
            return d1, [X[0], Y[0]], [X[1], Y[1]]
        elif d2 <= d1 and d2 <= d3:
            return d2, [X[0], Y[0]], [X[2], Y[2]]
        elif d3 <= d2 and d3 <= d1:
            return d3, [X[2], Y[2]], [X[1], Y[1]]

    m = X[length]
    LY = []
    RY = []
    LX = []
    RX = []
    for i in range(len(X)):
        if X_prime[i] < m:
            LY.append(Y_prime[i])
            LX.append(X_prime[i])
        else:
            RY.append(Y_prime[i])
            RX.append(X_prime[i])
    d1, x_min1, y_min1 = closest_pair(X[:length], Y[:length], LX, LY, x_min, y_min)
    d2, x_min2, y_min2 = closest_pair(X[length:], Y[length:], RX, RY, x_min, y_min)
    if d1 <= d2:
        d = d1
        x_min, y_min = x_min1, y_min1
    else:
        d = d2
        x_min, y_min = x_min2, y_min2

    mid_points = []
    for i in range(len(X_prime)):
        if m + d >= X_prime[i] >= m - d:
            mid_points.append([X_prime[i], Y_prime[i]])
    mid_length = len(mid_points)
    for p in range(mid_length):
        for neighbors in range(min(p + 1, mid_length - 1), p + min(mid_length - p - 1, 7)):
            if d > distance(mid_points[p], mid_points[neighbors]):
                d = distance(mid_points[p], mid_points[neighbors])
                x_min, y_min = mid_points[p], mid_points[neighbors]

    return d, x_min, y_min


n = int(input())
x = []
y = []
for i in range(n):
    nums = str(input()).split()
    x.append(int(nums[0]))
    y.append(int(nums[1]))
x_sorted, y_sorted = sort(x.copy(), y.copy())
y_sorted_by_y, x_sorted_by_y = sort(y.copy(), x.copy())
_, x, y = closest_pair(x_sorted, y_sorted, x_sorted_by_y, y_sorted_by_y)
if x[0] < y[0]:
    print(x[0], x[1], y[0], y[1])
else:
    print(y[0], y[1], x[0], x[1])
