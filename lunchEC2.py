import boto3

# Create a session with EC2
ec2_client = boto3.client('ec2')

# Launch an EC2 instance
response = ec2_client.run_instances(
    ImageId='ami-08b5b3a93ed654d19',  # Replace with your AMI ID
    InstanceType='t2.micro',         # Example instance type
    #KeyName='your-key-pair-name',    # Replace with your key pair name
    MinCount=1,
    MaxCount=1
    #SecurityGroupIds=['sg-0abc123456789def0'],  # Replace with your security group ID
    #SubnetId='subnet-0abc123456789def0',        # Replace with your subnet ID
)

print(f"Instance ID: {response['Instances'][0]['InstanceId']}")