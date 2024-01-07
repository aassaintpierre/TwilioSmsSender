from flask import Flask, render_template, request, redirect, url_for
from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER

app = Flask(__name__)

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input
        name = request.form['name']
        address = request.form['address']
        phone_number = request.form['phone_number']

        # Send SMS
        message_body = f"DO NOT REPLY! Hello {name}! We have receive your request, thank you for registering. Address: {address}, ID: 0010203302"
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )

        # Redirect to the same page after submission
        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)