#demo file to show diff in resource n client

import boto3

awsConsole = boto3.session.Session(profile_name="default")
resource_object  = awsConsole.resource('iam')
for eachUser in resource_object.users.all():
    print(eachUser.name)

print("------------------")

# below demo is for CLIENT

clientObject = awsConsole.client('iam')
for eachClient in clientObject.list_users()['Users']:
    print (eachClient['UserName'])