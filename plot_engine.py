from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

center_x, center_y = 5, 5 # center point of the shape on the plot
radius = 5 # distance from center to each vertex, controls size


# generates the angle position of each corner of a polygon on a circle, starting from the top
def generate_angles(amount_of_vertices, title_body):
	if amount_of_vertices == 4:
		vertex_angles = [45]  # square starts at 45 so sides are horizontal and vertical, not rotated like a diamond
	elif amount_of_vertices == 8:
		vertex_angles = [22.5]  # octagon starts at 22.5 so sides are flat, matching the stop sign orientation
	else:
		vertex_angles = [90]  # all other polygons start at the top of the circle
	angle_increment = int(360 / amount_of_vertices)  # degrees between each corner
	for vertex in range(amount_of_vertices - 1):  # -1 because first corner is already in the list
		next_angle = vertex_angles[-1] + angle_increment  # next corner's position on the circle
		if next_angle > 360:
			vertex_angles.append(next_angle - 360)  # if it surpasses 360 subtract 360 so it lands in the correct position on the circle
		else:
			vertex_angles.append(next_angle)
	calculate_data_points(vertex_angles, title_body)


def calculate_data_points(vertex_angles, title_body):

	# list comprehension — for each angle: converts degrees to radians, np.cos returns a value
	# between -1 and 1 representing horizontal direction, multiplied by radius to scale to the
	# correct distance, then center_x is added to shift from origin (0,0) to the actual center
	x = [center_x + radius * np.cos(np.radians(a)) for a in vertex_angles]

	# same as x but np.sin returns vertical direction instead of horizontal,
	# center_y shifts from origin to the actual center
	y = [center_y + radius * np.sin(np.radians(a)) for a in vertex_angles]

	x.append(x[0])  # repeat first point to close the shape
	y.append(y[0])
	z = [0] * len(x)

	plt.plot(x, y)
	plt.title(title_body)

	# So a circle looks like a circle and a square looks like a square. 
	# Without it matplotlib auto-scales each axis independently and your shapes get stretched or squished.
	plt.axis('equal') 
	plt.show() # Renders and displays the active plot in a window


