import boto3
import json
print('Loading function')

def lambda_handler(event, context):
    ssmClient = boto3.client('ssm')
    print("Received event: " + json.dumps(event, indent=2))
    print(event);
    message = event['Records'][0]['Sns']['Message']
    print("From SNS: " + message)
    #return message
    
    if message == "start": 
        COMMANDS=["sudo iptables -I INPUT -p tcp --dport 80 -j ACCEPT"]
    
    if message == "stop":
        COMMANDS=["sudo iptables -I INPUT -p tcp --dport 80 -j DROP"]
    
    
    ssmCommand = ssmClient.send_command(
             Targets =[
                 {
                     "Key": "tag:Name",
                     "Values":[
                         "Demo",
                         ]
                 },
             ],
         DocumentName = 'AWS-RunShellScript',
         TimeoutSeconds = 5000,
         Comment = 'Start/Stop  test nginx',
         
         Parameters = {
             "commands": COMMANDS
         }
       
     )
    print(ssmCommand)
