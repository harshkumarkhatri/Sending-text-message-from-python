import nexmo

import nexmo

client = nexmo.Client(key='20cef142', secret='s8Y1EOuOYAcc3SlP')

number=input("ENTER THE PHONE NUMBER")
message=input("ENTER THE MESSAGE YOU WNAT TO GIVE")

response=client.send_message({
    'from': 'GYMAALE',
    'to': number,
    'text': message,
})

response=response['messages'][0]
if response['status']=='0':
    print("MESSAGE DELIVERED SUCCESSFULLY",response['message-id'])
else:
    print("ERROR SENDING MESSAGE",response['error-text'])