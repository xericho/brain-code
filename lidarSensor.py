# -*- coding: utf-8 -*-


from numpy.random import uniform

"""
Class name: 	lidarSensor
Purpose:        This class simulates a lidar that 'scans' the environment
Description:	It only has one function which generates random data and 
                saves to 'scan' variable.
"""
class lidarSensor():
    """
    Function name:  __init__
    Purpose:        A constructor for lidarSensor, initializes class variables
    Description:    Initializes 'scan' variable to store measurements 
    Input:          None
    Output:         None
    """
    def __init__(self):
        self.scan = []

    """
    Function name:  getValues
    Purpose:		Generates data that simulates data coming from a lidar sensor.
    Description:	Using the numpy, it will store random numbers that range from 0.03 to 50
    Input:			N - number of samples in a 'scan'
    Output:			None
    """
    def getValues(self, N=200):

        # generate data from an uniform distribution of values [0.03, 50]
        self.scan = uniform(0.03,51,N)              # Does not include 51 












