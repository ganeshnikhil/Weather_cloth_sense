

def decison_msg(report:dict , temp_threshold = 38 , wind_threshold = 35 , humidity_threshold = 70 , cloud_threshold = 65 , uv_threshold = 8):
   decision_list = []
   decision_list.append(f'<p><strong style="color: green">{report["datetime"]}<strong></p>')
   rain = False 
   if report["temp"] >= temp_threshold or report["feels_like"] >= temp_threshold:
      msg = "<p><i>wear light cloth and take umbrealla with you 🥵</i></p>"
      decision_list.append(msg)
   
   if "rain" in report["condition"].lower():
      rain = True 
      msg = "<p><i>wear waterproff cloths and take umbrealla with you ⛈️</i></p>"
      decision_list.append(msg) 
   
   if report["wind"] >= wind_threshold:
      msg = "<p><i>wear a light cloth and take cap and mask with you 💨 </i></p>"
      decision_list.append(msg)
      
   if rain == False and report["humidity"] >= humidity_threshold:
      msg = "<p><i>wear a light cloth and take a handkerchief with you 💧</i></p>"
      decision_list.append(msg)
   
   if rain == False and report["cloud"] >= cloud_threshold:
      msg = "<p><i>wear a light waterproff cloth and take a umbrella with you 🌥️</i></p>"
      decision_list.append(msg)
      
   if report["uv"] >= uv_threshold:
      msg = "<p><i>wear full sleeves cloth and take a sunglasses and cap with you 🌞</i></p>"
      decision_list.append(msg)
   
   return decision_list

def generate_html(report:dict):
   
   decision_list = decison_msg(report)
   html_content = r"""
   <!DOCTYPE html>
   <html lang="en">
   <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Cloth Recommendations</title>
      <style>
         body {{
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 0;
            background-color: #f0f0f0;
         }}
         .recommendation {{
               max-width: 600px;
               margin: 20px auto;
               padding: 20px;
               background-color: #1e9bafef;
               border-radius: 10px;
               box-shadow: 0 0 10px #0000001a;
         }}
         .recommendation p {{
               margin: 10px 0;
               font-size: 18px;
               color: #000000;
            }}
            .recommendation i {{
               font-style: normal;
               color: #333333;
            }}
      </style>
   </head>
   <body>
      <div class="recommendation">
            {0}
      </div>
   </body>
   </html>
   """.format("\n".join(decision_list))
   # html_content = """
   # <html>
   
   # <head> 
   #    <title> Cloth Recommendations </title>
   # </head>
   
   # <body>
   #    {0}
   # </body>
   # </html> 
   # """.format('\n\n'.join(decision_list))
   return html_content

