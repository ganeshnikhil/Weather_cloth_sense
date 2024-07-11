import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(html_content , password, sender_email , receiver_email , smtp_server="smtp.gmail.com", port=587):
   try:

      msg = MIMEMultipart()
      msg['From'] = sender_email
      msg['To'] = receiver_email
      msg['Subject'] = "Clothing Recommendations"
      
      msg.attach(MIMEText(html_content, 'html'))
      
      context = ssl.create_default_context()
      with smtplib.SMTP(smtp_server, port) as server:
         server.ehlo()  # Can be omitted
         server.starttls()
         server.ehlo()  # Can be omitted
         server.login(sender_email, password)
         server.sendmail(sender_email, receiver_email, msg.as_string())
         print(f"Email send succesfully to {receiver_email}")
         return True 
   except Exception as e:
      print(f"Error: {e}")
   return False 
