# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 22:40:22 2025

@author: cpbre
"""


import smtplib
from email.message import EmailMessage

# Get user email
user = input("Please enter your email: ")
print(f"The email you entered is: {user}")

# Email sending out from
me = "cbrecken@ramapo.edu"
print(f"The email sending our message is: {me}") 

# Your email credentials
email_address = "put your school email here"  # Check that you authorize lower security emails and the like in gmail        
email_password = "put your password here"

# Create the email
msg = EmailMessage()
msg['Subject'] = "Hello from Python!"
msg['From'] = email_address
msg['To'] = user 
msg.set_content("This is an email sent through Python.")

# Send the email
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server: # I keep getting bad credentials errors when trying to send with my correct email and password
        server.login(email_address, email_password) # The number is 465, not 587
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print("Error sending email:", e)