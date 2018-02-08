# -*- coding: utf-8 -*-

import lidarSensor as sensor
import filters

# Create lidar object to generate data
lidar = sensor.lidarSensor()
lidar.getValues(5)	              	# scans environment, default is 200 measurements
print("Raw values:          {}".format(lidar.scan))

# init range filter
f1 = filters.rangeObject(5,40)	   	# set range_min = 5, range_max = 40
filtered = f1.update(lidar.scan)
print("After range filter:  {}".format(filtered))


# Dummy data for testing
testScan = [[0.,  1., 2., 1., 3.],
            [1.,  5., 7., 1., 3.],
            [2.,  3., 4., 1., 0.],
            [3.,  3., 3., 1., 3.],
            [10., 2., 4., 0., 0.]]

# init median filter 
f2 = filters.medianObject(3) 		# set D = 3
for scan in testScan:
    print(f2.update(scan))


