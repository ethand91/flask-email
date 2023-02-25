from flask import Flask, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route("/send", methods=["POST"])
def send():
    email_address = request.form['address']
    email_subject = request.form['subject']
    email_message = request.form['message']

    sender_email = 'youremail'
    sender_password = 'your password'
    receiver_email = email_address

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = email_subject
    message.attach(MIMEText(email_message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()

        return 'Email Sent!'
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
