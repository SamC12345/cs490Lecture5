# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import os


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hello World from Twilio.",
                     from_='+16614855083',
                     to='+12013769408'
                 )

print(message.sid)