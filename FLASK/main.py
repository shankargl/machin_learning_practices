from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/send-message", methods=["POST"])
def send_message():

    name = request.form.get("name")
    sender_email = request.form.get("email")
    subject = request.form.get("subject")
    message = request.form.get("message")

    receiver_email = "shankarshankargl2007@gmail.com"
    
   
    app_password = "mfvm isgg tlps hbul"

    email = EmailMessage()

    email["From"] = receiver_email
    email["To"] = receiver_email
    email["Subject"] = f"Portfolio Contact: {subject}"

    email.set_content(
        f"""
New message from your portfolio website

Name: {name}
Email: {sender_email}
Subject: {subject}

Message:
{message}
"""
    )

    try:

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

            smtp.login(receiver_email, app_password)

            smtp.send_message(email)

        return """
        <script>
            alert("Message sent successfully!");
            window.location.href = "/#contact";
        </script>
        """

    except Exception as e:

        print("\n================ EMAIL ERROR ================")
        print(e)
        print("=============================================\n")

        return f"""
        <h2>Email could not be sent</h2>
        <p>Error: {e}</p>
        <br>
        <a href="/#contact">Go back</a>
        """


if __name__ == "__main__":
    app.run(debug=True)