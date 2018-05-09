from flask import Flask
from flask_mail import Mail,Message

app = Flask(__name__)
app.config.from_pyfile('config.cfg.py')
mail = Mail(app)

@app.route("/send-mail")
def index():

    msg = Message("Hello",
                  sender="lirancash@gmail.com",
                  recipients=["l.farage@gmail.com"])
    mail.send(msg)
    return 'Message Sent!'

if __name__ == '__main__':
    app.run(debug=True) # Do not use debug in production env
