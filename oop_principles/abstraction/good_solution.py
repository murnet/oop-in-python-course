class EmailService:
    def send_email(self):
        # Call private methods within the class
        self._connect()
        self._authenticate()
        print("Sending email...")
        self._disconnect()

    def _connect(self):
        print("Connecting to email server...")

    def _authenticate(self):
        print("Authenticating...")

    def _disconnect(self):
        print("Disconnecting from email server...")

email = EmailService()
email.send_email()

# LOGS:
# Sending email...
# Connecting to email server...
# Authenticating...
# Disconnecting from email server...

# In VSCode, when I type "email.", VSCode shows the EmailService api, or the methods that are available for the client code to call. As a Python dev, I know that methods that start with _ should not be accessed outside the class, so I know to send an email, I just call send_email, and all the other stuff is abstraction -- stuff not relevant to me/the client; these methods are "implementation details" only relevant internally to the class. These implementation details are abstracted away from clients by making them private or protected, making life simple for clients -- it signals to them that we only have to worry about calling send_email, and we don't need any knowledge of the steps involved in sending an email. This makes life much easier for clients/devs using this code. SEE C# ebook for the explanation -- dunno why I felt the need for all this text here...
