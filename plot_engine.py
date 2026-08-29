from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import numpy as np

center_x, center_y = 5, 5 # center point of the shape on the plot
radius = 5 # distance from center to each vertex, controls size

# generates the angle position of each corner of a polygon on a circle, starting from the top
# dimension is required and goes first, vertex_angles and amount_of_vertices are optional, defaults to None
# required parameters must come before optional ones, Python assigns positional arguments left to right
def generate_angles(dimension, vertex_angles=None, amount_of_vertices=None): 
	
	if vertex_angles:

		calculate_data_points(dimension, vertex_angles)

	else: 

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

		calculate_data_points(dimension, vertex_angles)

def calculate_data_points(dimension, vertex_angles):
	# list comprehension — for each angle: converts degrees to radians, np.cos returns a value
	# between -1 and 1 representing horizontal direction, multiplied by radius to scale to the
	# correct distance, then center_x is added to shift from origin (0,0) to the actual center
	x = [center_x + radius * np.cos(np.radians(a)) for a in vertex_angles]

	# same as x but np.sin returns vertical direction instead of horizontal,
	# center_y shifts from origin to the actual center
	y = [center_y + radius * np.sin(np.radians(a)) for a in vertex_angles]

	x.append(x[0])  # repeat first point to close the shape
	y.append(y[0])
		
	plot_figures(dimension, x, y)


def plot_figures(dimension, x, y):

	if dimension.lower() == '2d':

		plt.plot(x, y, color='#00FF00')  # sets plot line color to green

		# plt.axis('equal') added so a circle looks like a circle and a square looks like a square. 
		# Without plt.axis('equal') matplotlib auto-scales each axis independently and your shapes get stretched or squished.
		plt.axis('equal') 

		# 'plt.axis('off')' hides the x and y axes, cleaner look for 2D plots
		# 'plt.gcf().set_facecolor('black')' sets the outer figure window to black and
		# 'plt.gca().set_facecolor('black')', which is NOT in the script, sets the inner plot area to black, but
		# since 'plt.axis('off')' is on, gcf (get current figure) alone turns both inner and outer black, hence we don't need gca (get current axis)
		plt.axis('off')
		plt.gcf().set_facecolor('black')

		# renders the canvas and everything drawn on it. Since this is 2D, 
		# you don't have to create the empty canvas, plt.plot() runs plt.figure() behind the scenes. 
		# on 3D you do have to run plt.figure() and plt.plot() separately, as shown below in 'elif dimension == '3D''.
		# extra: it opens the window and blocks the script from moving forward until the window is closed.
		plt.show() 

	elif dimension.lower() == '3d':

		z_top = [4] * len(x)    # top face, list of 4s the same length as x, placing the shape at z=4
		z_bottom = [0] * len(x) # bottom face, list of zeros the same length as x, placing the shape flat on z=0

		# creates an empty canvas, in 2D plt.plot() runs plt.figure() behind the scenes, 
		# in 3D we need to create it explicitly to attach the 3D axes
		fig = plt.figure() 

		# With 'ax = fig.add_subplot(111, projection='3d')' we add a plot to the empty canvas
		# 111 means 1 row, 1 column, 1st plot, one cartesian plane taking up the whole canvas
		# if you said 211 it would mean 2 rows, 1 column, 2 stacked plots, working on the 1st one (top)
		# if you said 121 it would mean 1 row, 2 columns, 2 side by side plots, working on the 1st one (left)
		# projection='3d' adds the z axis to that cartesian plane
		ax = fig.add_subplot(111, projection='3d')

		ax.plot(x, y, z_bottom, color='#00FF00') # draws bottom face on the 3D cartesian plane and sets plot line color to green
		ax.plot(x, y, z_top, color='#00FF00') # draws the top face on the 3D cartesian plane and sets plot line color to green
 
		ax.axis('equal') 
	
		# 'ax.set_axis_off()' hides all axes and the cartesian grid in 3D
		# 'ax.set_facecolor('black')' sets the inner plot area to black
		# 'fig.patch.set_facecolor('black')' sets the outer figure window to black
		# in 3D both set_facecolor methods are needed even with ax.set_axis_off(), 
		# unlike 2D where axis('off') alone is enough to turn everything black
		ax.set_axis_off()  
		ax.set_facecolor('black') 
		fig.patch.set_facecolor('black')

		# to connect z_top and z_bottom we need vertical lines at each vertex
		# we loop through range(len(x) - 1), excluding the last point since that's used to close the shape
		# i is the temp variable used as the index to access x and y values at each position
		# each iteration generates one ax.plot() made up of 2 x values, 2 y values, and z [0, 4]
		# x and y change each iteration depending on the figure, z [0, 4] is fixed, 0 is z_bottom and 4 is z_top
		for i in range(len(x) - 1):
			ax.plot([x[i], x[i]], [y[i], y[i]], [0, 4], color='#00FF00')

		# ax.view_init sets the camera position on an invisible sphere around the figure
		# elev controls how high or low the camera sits on that sphere
		# azimuth (azim) is the horizontal angle around the shape, like walking in a circle around the figure
		# to rotate horizontally, fix elev to a static value such as elev=20 and pass angle to azim
		# to rotate vertically instead, fix azim to a static value such as azim=45 and pass angle to elev
		def rotate(angle):
			ax.view_init(elev=70, azim=angle)

		# ani is a variable that holds the FuncAnimation object, which takes fig (canvas), rotate (function reference),
		# frames (angles passed into rotate as angle one at a time), interval (milliseconds between each call)
		# and repeat (loop or stop, default False)
		# the way it works is: when the interpreter reaches ani, FuncAnimation runs, binding everything together and calling rotate
		# plt.show() opens the window showing the 3D figure, and behind the scenes interval=50 keeps ani alive,
		# passing the next frame value into rotate every 50ms, updating the camera angle
		# ani must be stored in a variable, without it Python only calls rotate once and deletes the animation object immediately
		ani = FuncAnimation(fig, rotate, frames=range(0, 360, 2), interval=50, repeat=True)

		plt.show() # renders the canvas (fig) and displays everything drawn on it, all ax.plot() calls, titles, and styling applied to the figure




