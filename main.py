from Src.weather_report import get_weather_report 
from Src.get_coordinate import get_lat_lng 
from Src.generate_msg import generate_html 
from Src.send_email import send_email 
from Src.write_html import write_to_file 
from os import environ
from dotenv import load_dotenv
from sys import argv 

load_dotenv()

def main():
   
   PORT = 587
   SMTP_SERVER = "smtp.gmail.com"
   
   try:
      API_KEY = environ.get("Api_key")
      SENDER_EMAIL = environ.get("Sender_email")
      RECIEVER_EMAIL = environ.get("Receiver_email")
      PASSWORD = environ.get("Password")
      PATH = f"Backup/{RECIEVER_EMAIL}.html"
   except Exception as e:
      print(f"Error:{e}")
      print("Check your .env file....")
      exit()
   
   arg = argv 
   if len(arg) == 2:
      city = arg[1].lower().strip().replace("_"," ")
   else:
      print("Only pass  one argument name of city....")
      exit()
   
   lat , long = get_lat_lng(city)
   report = get_weather_report(lat , long , API_KEY)
   email_content = generate_html(report)
   write_to_file(email_content , PATH)
   send_email(email_content , PASSWORD , SENDER_EMAIL , RECIEVER_EMAIL , SMTP_SERVER , PORT)
   

if __name__ == "__main__":
   main()
   
   
   




