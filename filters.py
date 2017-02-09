import numpy as np

# simulates the lidar which generates an array of float values
from lidarSensor import lidarSensor 	

"""
Class name:	rangeObject
Purpose:	Crops all the values that are below range_min (or above range_max)
		and replaces them with the range_min value (or range_max value)
Description:	This class has one function (update) which scans once from the 
		lidar sensor and applies a range filter
"""
class rangeObject:

	"""
	Function name:	__init__
	Purpose:	A constructor for rangeObject, initializes values
	Description:	Stores the range_min and range_max values
	Input:		range_min: the cutoff value for the minimum
			range_max: the curoff value for the maximum
	Output:		None
	"""
	def __init__(self, range_min, range_max):
		self.range_min = range_min
		self.range_max = range_max

	"""
	Function name:	update
	Purpose:	Gets data from the lidar and applies the range filter
	Description:	Reads the lidar sensor data from a file.
			It then loops through the list and replaces the outliers 
			with either range_min or range_max
	Input:		None
	Output:		Returns the list of filtered float values
	"""
	def update(self):
	
		f = open('output.txt', 'r')
		string = f.readline()
		arr = string.strip().split()		# stores line from file to a list
		for i in range(len(arr)):		# converts string to floats
			arr[i] = float(arr[i])

		for index in range(len(arr)):
			# replace value if below min range
			if arr[index] < self.range_min:
				arr[index] = self.range_min
			# replace value if ablove max range
			elif arr[index] > self.range_max:
				arr[index] = self.range_max
		
		f.close()		
		return arr

class medianObject:

	def __init__(self, delay):
		self.delay = delay

	def update(self):
		
		f = open('output.txt','r')
		
		# put values in a 2D array
		storeValues = []
		for i in range(self.delay):
			string = next(f).strip().split()
			for j in range(len(string)):
				string[j] = float(string[j])
			storeValues.append(string)

		# finds the median
		arr = []
		for i in range(len(storeValues[0])):
			current = []
			for t in range(self.delay):
				current.append(storeValues[t][i])
			arr.append(np.median(current))

		return arr
# Driver code for testing
"""
# For testing rangeObject
lidar = lidarSensor()
lidar.getValues()
x = rangeObject(5,40)
print x.update()


"""
# For testing medianObject
lidar = lidarSensor()
lidar.getValues()
y = medianObject(3)
print y.update()

