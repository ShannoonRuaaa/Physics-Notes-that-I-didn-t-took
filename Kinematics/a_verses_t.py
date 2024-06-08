import matplotlib.pyplot as plt
import numpy as np

# Define the constant acceleration (e.g., 5 m/s)
constant_acceleration = 9.8  # meters per second

# Create a range of time values (e.g., from 0 to 10 seconds)
time = np.linspace(0, 10, 100)  # 100 points from 0 to 10 seconds

# Create an array of acceleration values, which are constant
acceleration = np.full_like(time, constant_acceleration)

# Define font properties
font = {'family': 'serif', 'color': 'black', 'weight': 'normal', 'size': 14}

# Plot the acceleration over time
plt.figure(figsize=(10, 6))
plt.plot(time, acceleration, label=f'Acceleration = {constant_acceleration} m/s')

# Shade the region under the curve
plt.fill_between(time, acceleration, color='skyblue', alpha=0.4)

# Set labels with custom font
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Acceleration (m/s)', fontdict=font)
plt.title('Constant Acceleration Over Time', fontdict=font)

plt.legend()
plt.grid(True)
plt.show()
