import smtplib
from email.mime.text import MIMEText

THRESHOLD_TEMP = 35

def send_alert(city, temp):
    msg = MIMEText(f"Alert! {city} temperature is {temp}°C, exceeding the threshold!")
    msg['Subject'] = 'Weather Alert'
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'recipient_email@example.com'

    with smtplib.SMTP('smtp.example.com') as server:
        server.login('your_email@example.com', 'your_password')
        server.send_message(msg)

def check_alerts(weather_data):
    for city, details in weather_data.items():
        if details['main']['temp'] > THRESHOLD_TEMP:
            send_alert(city, details['main']['temp'])