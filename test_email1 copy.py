import pandas as pd  ##reading our excel file
# import datetime   ##for intracting with time and year
import smtplib ##for a connection between our gmail & python script
from email.message import EmailMessage ## sending emails
# import os  ## intracting with the system

def sendEmail(to, sub, msg):    
  print(f"email to {to} \nsend with subject: {sub}\n message: {msg}")    
  email = EmailMessage()    
  email['from'] = 'The Company Office'    
  email['to'] = f"{to}"    
  email['subject'] = f'{sub}'     
  email.set_content(f'{msg}')     
  with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:          
        smtp.ehlo()        
        smtp.starttls()        
        smtp.login('testuser@gmail.com','password')        
        smtp.send_message(email)        
        print("Email send")    
  pass


sendEmail("sampleusername@gmail.com","Welcome Aboard","Welcome to the online test hosted by the company. Please answer the following qns to continue")