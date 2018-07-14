#!/usr/bin/env python
'''
A python implementation for AWS instance creation & control via module awsinfrastructurecreation
'''

import configparser
import awsinfrastructurecreation

config = configparser.ConfigParser()
config.read('genericAWSAutomation.cfg')

LinuxImageId       = config['BLOCKCHAINAUTOMATIONAWS']['LinuxImageId']
imageId            = config['BLOCKCHAINAUTOMATIONAWS']['UbuntuImageId']
instanceType       = config['BLOCKCHAINAUTOMATIONAWS']['instanceType']
ec2KeyName         = config['BLOCKCHAINAUTOMATIONAWS']['ec2KeyName']
networkInterfaces  = config['BLOCKCHAINAUTOMATIONAWS']['networkInterfaces']
subnetId = config['BLOCKCHAINAUTOMATIONAWS']['subnetId']
groups = config['BLOCKCHAINAUTOMATIONAWS']['groups']


awsClient = awsinfrastructurecreation.blockchainAutomationAWS_Client()

awsClient.ec2InstanceCreation(imageId, instanceType, ec2KeyName, subnetId, groups)
