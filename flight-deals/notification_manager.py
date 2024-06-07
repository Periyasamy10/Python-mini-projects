from twilio.rest import Client

TWILIO_SID = "AC76dceec63258dd8f342c5e561173e730"
TWILIO_AUTH_TOKEN = "ba3fb2316e6cf593de366a017d542939"
TWILIO_VIRTUAL_NUMBER = "+16185912647"
TWILIO_VERIFIED_NUMBER = "+918220997661"


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )
        print(message.sid)
