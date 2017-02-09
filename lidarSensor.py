import random

"""
Class name: 	lidarSensor
Purpose:	This class simulates a LIDAR that 'scans' and gives a reading 
		from its sensor.
Description:	It only has one function which generates random data and 
		writes the output to a file
"""
class lidarSensor:

	"""
	Function name:		getValues
	Purpose:		Generates data that simulates data coming from
				a lidar sensor.
	Description:		Using the random library, it will store random 
				numbers that range from 0 to 60 in a file of 
				length N
	Input:			None
	Output:			Writes the generated data in a file called output.txt
	"""
	def getValues(self):

		# write to output.txt/ create file if nonexistant 
		f = open('output.txt','w')

		N = 5			# length of measurements N
		numScan = 10		# 'scans' 10 times

		while numScan > 0:
			for i in range(N):
				# generated data can range from 0.03 to 50
        			f.write(str(random.uniform(0.03, 50))+' ')
			f.write('\n')
			numScan -= 1
		f.close()

