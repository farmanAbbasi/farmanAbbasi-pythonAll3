from twilio.rest import Client
# from twilio folder , there is folder called rest which has a class called Client

# Your Account SID from twilio.com/console
account_sid = "AC7a15814cc0850e87d0168b1744d12561"
# Your Auth Token from twilio.com/console
auth_token  = "c6346342a32471b7a929b52e1659cef4"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+917906721486", 
    from_="+12015483553",
    body="this is awesome")

print(message.sid)
