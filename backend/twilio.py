<html>
from twilio.rest import Client
var recipe = ""
var numero = ""
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15558675309", 
    from_="+15017250604",
    body="Hello, you have + $(numero) + $(recipe) + saved ")

print(message.sid)
</html>
