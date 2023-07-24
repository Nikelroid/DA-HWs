import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt


# Get the number of white and black points from the user
inp = input().split()
n,m = int(inp[0]),int(inp[1])

# Get the coordinates of the white points from the user
white_points = []
for i in range(n):
    x, y = map(float, input().split())
    white_points.append([x, y])

# Get the coordinates of the black points from the user
black_points = []
for i in range(m):
    x, y = map(float, input().split())
    black_points.append([x, y])

# Combine the white and black points into a single dataset
data = np.array(white_points + black_points)

# Create the labels for the dataset (1 for white points, -1 for black points)
labels = np.array([-1]*n + [1]*m)

# Define the variables for the optimization problem
a = cp.Variable()
b = cp.Variable()
t = cp.Variable()
# Define the constraints for the optimization problem
constraints = [labels[i]*(data[i,0]*a + b - data[i,1]) >= t for i in range(n+m)]

# Define the objective function for the optimization problem
objective = cp.Maximize(t)

# Solve the optimization problem
problem = cp.Problem(objective, constraints)
problem.solve()

# Get the optimal values for w and b
a_opt = a.value
b_opt = b.value

# Compute the line equation (y = mx + c) from the optimal values of w and b


# Print the line equation
print("({:.4f},{:.4f})".format(a_opt, b_opt))

plt.scatter(data[:,0], data[:,1],c = labels)
x = np.arange(-4, 10)
y = (a.value * x + b.value)
y1 = (a.value * x + b.value + t.value)
y2 = (a.value * x + b.value - t.value)
plt.plot(x, y, color='red')
plt.plot(x, y1, color='green')
plt.plot(x, y2, color='green')
plt.show()
