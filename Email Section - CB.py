# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 01:04:12 2025

@author: cpbre
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 22:40:22 2025

@author: cpbre
"""

import smtplib       # Import this in to send email at the end
from email.message import EmailMessage

user = input("Please enter your email: ")   # Prompting user for their email
print(f"The email you entered is: {user}.")


me = ""                  # The email you will receive mail from
email_password = ""      # To use this, you need to generate an app password. Put the app password here. 
# You need to use 2fa. Need to use a gmail account.

print(f"The email sending our message to you is: {me}. Always check spam folder in case.") 


# Gather the information for printing
#total_results = []




# Create the email formatting
msg = EmailMessage()
msg['Subject'] = "Prepare for your trip with Team Four's Project!"
msg['From'] = me
msg['To'] = user 
msg.set_content("Thank you for using our github project!\n"
                "Let's print the results!\n")
#msg.set_content(total_results)


try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server: # We are creating a server to send mail through
        server.login(me, email_password) # The number is 465, not 587, because we are using gmail
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print("Error sending email:", e)




