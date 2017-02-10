import numpy as np
from lidarSensor import lidarSensor 	

"""
Class name:	rangeObject
Purpose:	Crops all the values that are below range_min (or above range_max)
		and replaces them with the range_min value (or range_max value)
Description:	This class has one function to be called (update) which scans once
		from the lidar sensor and applies a range filter
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
	Description:	Reads the last line of the lidar sensor data from a file 
			It then loops through the list and replaces the outliers 
			with either range_min or range_max
	Input:		None
	Output:		Returns the list of filtered float values
	"""
	def update(self):
	
		f = open('output.txt', 'r')
		string = f.readlines()
		arr = string[-1].strip().split()	# stores last line from file to a list
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

"""
Class name:	medianObjects
Purpose:	Finds the median of the current and previous D scans
Description:	The number of previous scans D is a parameter that is
		given when creating a new medianObject. It gets the
		previous D scans and the current scan only and returns the
		median of each measurement 
"""
class medianObject:

	"""
	Function name:	__init__
	Purpose:	A constructor for medianObject, initializes delay
	Description:	Stores the number of previous scans 
	Input:		delay: the number of previous scans desired
	Output:		None
	"""
	def __init__(self, delay):
		self.delay = delay+1		# num of prev and current scans

	"""
	Function name:	update
	Purpose:	Finds the median of the current and previous D scans
	Description:	It reads the current and previous D scans from a file
			and stores them in to a 2D list. It then loops each index
			of each scan and finds the median of that index. 
	Input:		None
	Output:		Returns a list of the median from the scans
	"""
	def update(self):
		
		storeValues = []		# variable for storing the scans
		delay = self.delay
		# reads each line starting from the bottom of test.txt 
		for line in reversed(open("test.txt").readlines()):
			# get out of loop after number of desired scans
			if delay <= 0:
				break

			# take out the newline and spaces and store them in a list
			string = line.strip().split()
			
			# convert each element of list to a float value
			for j in range(len(string)):
				string[j] = float(string[j])
			
			storeValues.append(string)
			delay -= 1

		# finds the median
		arr = []			# variable to store the median
		for i in range(len(storeValues[0])):
			current = []		# variable to store elements from each 'column'
			numCol = len(storeValues)-1	# the number of total scans
			for t in range(self.delay):
				# get out of loop if no more scans
				if numCol < 0:
					break
				current.append(storeValues[numCol][i])
				numCol -= 1
			# calculates the median for that 'column' and store in a list
			arr.append(np.median(current))
		
		return arr

# Driver code for testing
"""
# Create lidar object to generate data
lidar = lidarSensor()
lidar.getValues()	# outputs to output.txt

# For testing rangeObject
x = rangeObject(5i,40)	# set range_min = 5, range_max = 40
print x.update()

# For testing medianObject
y = medianObject(3)
print y.update()
"""
