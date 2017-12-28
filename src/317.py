from math import sin, cos, pi
import matplotlib.pyplot as plt

timestep = 0.01
num_angles = 1000
num_samples = 1000

# Returns the point at which the shrapnel from the firecracker with initial angle
# theta is located at time t.
def PtOfShrapnel(t, theta):
    # Standard parametric formula for coordinates
    x = 20 * cos(theta) * t
    y = -4.9 * t * t + 20 * sin(theta) * t + 100
    return (x,y)

# Simple wrapper so we don't plot points below the x axis.
def FValidPt(pt):
    return pt[1] >= 0

angles = [2 * i * pi / num_angles for i in range(num_angles)]
times = [timestep * i for i in range(num_samples)]

x_coords = []
y_coords = []
for angle in angles:
    for time in times:
        pt = PtOfShrapnel(time, angle)
        if FValidPt(pt):
            x_coords.append(pt[0])
            y_coords.append(pt[1])

parab_x = [i for i in range(-100, 101)]
parab_y = [-981.0 * x * x / 80000.0 + 118100.0/981.0 for x in parab_x]
plt.plot(x_coords, y_coords, 'ro', parab_x, parab_y, 'bs')
plt.axis([-120, 120, 0, 150])
plt.show()
# Plots should be sufficiently convincing that we have a paraboloid :)
