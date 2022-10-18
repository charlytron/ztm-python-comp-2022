from twilio.rest import Client 
 
account_sid = '########' 
auth_token = '***************' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='*****itsallacademic*****', 
                              body='Hey, Baybuh',      
                              to='+160#########' 
                          ) 
 
print(message.sid)