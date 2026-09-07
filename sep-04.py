email_id="saketh@codegnan.com"
print(email_id[7:15])
emails=['bharat@codegnan.com','shankar@codegnan.com','rohith@codegnan.com']
emails.extend(['deepika@codegnan.com','layatri@codegnan.com','parimala@codegnan.com'])
print(emails)
users={}
for i in range(1,len(emails)):
    users[i]=emails[i]
print(users)

data=dict(enumerate(emails,1))
print(data)
    
