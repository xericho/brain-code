import numpy as np

# simulates the lidar which generates an array for float values
from lidarSensor import lidarSensor 	

class rangeObject:

	def __init__(self, arr, min_range, max_range):
		self.arr = arr
		self.min_range = min_range
		self.max_range = max_range

	def rangeFilter(self):

		outOfRange = 0;

		for index in range(len(self.arr)):
			# replace value if below min range
			if self.arr[index] < self.min_range:
				self.arr[index] = self.min_range
				outOfRange += 1
			# replace value if ablove max range
			if self.arr[index] > self.max_range:
				self.arr[index] = self.max_range
				outOfRange += 1

		print 'Number of errors found: '+str(outOfRange)

	def update(self, arr):
		self.arr = arr
		self.rangeFilter()
		return self.arr

class medianObject:

	def __init__(self, delay):
		self.delay = delay

	def medianFilter(self, arr):
		# create object for getting values
		lidar = lidarSensor() 		

		# put values in a 2D array
		storeValues = [[lidar.getValues()] for i in range(self.delay)]

		for i in range(len(arr)):
			temp = []
			temp.append(arr[i])
			for t in range(self.delay):
				temp.append(storeValues[t][i])
			print temp
			arr[i] = np.median(temp)
		print arr

	def update(self, arr):
		self.arr = arr
		self.medianFilter()
		return self.arr		

# TESTING

arr = lidarSensor()
#print arr.getValues()		# generates an array of random numbers
x = rangeObject(arr.getValues(), 1, 50)
x.rangeFilter()
"""
arr = [0,0,290,3,3,4,0]
n = x.update(arr)
print n
print x.lidar
y = medianObject(arr)
print y.lidar
"""
y = medianObject(3)
y.medianFilter(arr)
