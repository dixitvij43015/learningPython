import boto3
from pprint import pprint
awsConsole = boto3.session.Session(profile_name="default")

ec2Console = awsConsole.client(service_name="ec2")

result = ec2Console.describe_instances()['Reservations']

for manyinstances in result:
    for eachinstances in manyinstances['Instances']:
        print (eachinstances['InstanceId'])