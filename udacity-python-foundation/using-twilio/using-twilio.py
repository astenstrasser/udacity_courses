from twilio.rest import Client

# SID da sua conta, encontre em twilio.com/console
account_sid = "xxx"
# Seu Auth Token, encontre em twilio.com/console
auth_token = "xxx"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="xx",
    from_="xx",
    body="Hello from Python!")

print(message.sid)
