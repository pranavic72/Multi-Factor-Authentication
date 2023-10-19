import random 
from twilio.rest import Client

otp = random.randint(1000,9999)

account_sid = "AC13da4def191172aa2a8f24c1876d1f8a"

auth_token = '5f4dfbb0b177b8d45929fbc5619cd1a5'

client = Client(account_sid,auth_token)

msg = client.messages.create(
    body = f"Your OTP is {otp}",
    from_ = "+919004901727",
    to = "+918698962280"
)