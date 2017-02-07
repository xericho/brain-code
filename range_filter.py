import random

min_range = 0.03
max_range = 50
lidar = []		# initialize for dynamic size

# generates test data
for i in range(random.randrange(200,1001)):  # gets a number between 200-1000
	lidar.append(random.uniform(0,75))

def rangeFilter(arr):

	outOfRange = 0;

	for index in range(len(lidar)):
		# replace value if below min range
		if lidar[index] < min_range:
			lidar[index] = min_range
			outOfRange += 1
		# replace value if ablove max range
		if lidar[index] > max_range:
			lidar[index] = max_range
			outOfRange += 1

	print 'Number of errors found: '+str(outOfRange)

rangeFilter(lidar)

