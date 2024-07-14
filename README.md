

### README.md

---

# Weather Cloth

WEATHER CLOTH is a Python application that fetches weather data for a specified city, generates an HTML email with CLOTH recommendations, saves it to a file, and sends it via email using SMTP authentication.

weather email  | weather email|
|--------------|-------------|
<img src="sample/1.png" width = "400"/>| <img src="sample/2.png" width="400"/> |

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ganeshnikhil/Weather_cloth_sense.git
   cd Weather_cloth_sense
   ```
2. Get api key from rapid api.
   ```bash 
   https://rapidapi.com/weatherapi/api/weatherapi-com
   ```

3. Install dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
   
   The requirements.txt file should contain:
   ```bash
   python-dotenv
   ```


4. Create a `.env` file in the root directory (`Weather_cloth_sense/.env`) and add your environment variables:
   ```plaintext
   # Example .env file for Rain Reminder project

   # API key for weather API (replace with your actual API key)
   Api_key="your_weather_api_key_here"

   # Sender email address for sending weather notifications
   Sender_email="your_sender_email@gmail.com"

   # Receiver email address for receiving weather notifications
   Reciever_email="recipient_email@example.com"

   # Password for the sender email account (replace with your email password)
   Password="your_email_password_here"
   ```

## Directory Structure

```
Weather_cloth_sense/
├── .env
├── README.md
├── requirements.txt
├── Backup/
│   ├── test.html
│        ...
├── Src/
│   ├── weather_report.py
│   ├── get_coordinate.py
│   ├── generate_msg.py
│   ├── send_email.py
│   └── write_html.py
└── main.py
```

- **`.env`:** Contains environment variables (API key, email credentials).
- **`README.md`:** This file, providing project overview, installation guide, and usage instructions.
- **`requirements.txt`:** Lists Python dependencies (python-dotenv).

- **`Backup/`:** Directory saves email content in a .html file.

- **`Src/`:** Directory containing Python modules:
  - `weather_report.py`: Fetches weather data using API.
  - `get_coordinate.py`: Retrieves latitude and longitude for a city.
  - `generate_msg.py`: Generates HTML email content with weather recommendations.
  - `send_email.py`: Sends email using SMTP server and credentials.
  - `write_html.py`: Writes HTML content to a file.

## Usage

To run the script, specify the city name as a command-line argument:

**`WINDOWS`:**
```bash
python main.py city_name
```
IF the name of city or area contains space between write it using this symbol `-` .

**`MAC or LINUX`:**
```bash
python3 main.py city_name
```

Replace `city_name` with the name of the city for which you want to fetch weather information and send reminders.

---

### Notes:

- Ensure Python 3.x is installed on your system.
- Replace placeholders (`your_weather_api_key_here`, `your_sender_email@gmail.com`, etc.) in `.env` with your actual API key and email credentials.
- Keep sensitive information secure and do not expose `.env` file in version control (add `.env` to `.gitignore`).
