#!/usr/bin/env python
import boto3

'''
A python client implementation for AWS
'''

class blockchainAutomationAWS_Client():
# Retrieve instance id & its state
    def ec2InstanceDetails(self):
        ec2Resource = boto3.resource('ec2')
        print(ec2Resource.instances)
        for instance in ec2Resource.instances.all():
            print(instance.id, instance.state)
            print(instance)

# Creation of t2.micro instance with Ubuntu free tier
    def ec2InstanceCreation(self, imageId, instanceType, keyName, subnetId, groups):
        self.ec2Instance = boto3.resource('ec2')
        self.instanceCreation = self.ec2Instance.create_instances(
            ImageId=imageId,
            MinCount=1,
            MaxCount=1,
            InstanceType = instanceType,
            KeyName = keyName,
            NetworkInterfaces = [{'SubnetId': subnetId, 'DeviceIndex': 0, 'AssociatePublicIpAddress': False, 'Groups': [groups]}])
        print(self.instanceCreation[0].id)

    def ec2InstanceTermination(self, instanceId):
        ec2InstanceTerminate = boto3.client('ec2')
        ec2InstanceTerminated = ec2InstanceTerminate.terminate_instances(
            InstanceIds=[instanceId,],
#            DryRun=True
            DryRun=False)
        print(ec2InstanceTerminated)        
        

  
