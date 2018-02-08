import numpy as np	

"""
Class name:		rangeObject
Purpose:		Crops all the values that are below a minimum value (or above a maximum value)
				and replaces them with the minimum value (or maximum value)
Description:	This class has an update function that applies a range filter
"""
class rangeObject():

	"""
	Function name:	__init__
	Purpose:		A constructor for rangeObject, initializes class variables
	Description:	Stores the range_min and range_max values
	Input:			range_min: the cutoff value for the minimum
					range_max: the curoff value for the maximum
	Output:			None
	"""
	def __init__(self, range_min, range_max):
		self.min = range_min
		self.max = range_max

	"""
	Function name:	update
	Purpose:		Gets data from the lidar and applies the range filter
	Description:	It finds the indices of values above and below the 
					max and min values, respectively, and replaces them.
	Input:			None
	Output:			Returns the list of filtered float values
	"""
	def update(self, scan):
	
		scan[scan < self.min] = self.min      	# replaces values under min with min
		scan[scan > self.max] = self.max      	# replaces values over max with max 

		return scan
  




"""
Class name:		medianObjects
Purpose:		Finds the median of the current and previous D scans
Description:	The number of previous scans D is a parameter that is
				given when creating a new medianObject. It gets the
				previous D scans and the current scan and returns the
				median of each measurement 
"""
class medianObject():

	"""
	Function name:	__init__
	Purpose:		A constructor for medianObject, initializes class variables
	Description:	Stores the D parameter and initializes an empty list to store previous D scans 
	Input:			D:  the number of previous scans desired
	Output:			None
	"""
	def __init__(self, D):
		self.D = D+1							# num of current and previous scans
		self.prevScans = [] 					# init empty list to store previous D scans

	"""
	Function name:	update
	Purpose:		Finds the median of the current and previous D scans
	Description:	This function receives a single scan, stores the scan, and
					finds the median of each measurement based on the previous D scans
	Input:			scan:  A single scan from the lidar
	Output:			Returns an array of the median from the scans
	"""
	def update(self, scan):
		
		if(len(self.prevScans) < self.D):
			self.prevScans.append(scan) 		# store scan if prevScans has < D scans
		else:
			self.prevScans.pop(0) 				# remove oldest scan
			self.prevScans.append(scan) 		# add new scan

		scans = np.array(self.prevScans)		# convert to a matrix
		
		return np.median(scans, 0) 				# return the median across each column

