import random

class lidarSensor:

	def getValues(self):
		arr = []
		# generates test data
		N = 10
		for i in range(N):
        		arr.append(random.uniform(0,75))
		
		return arr

