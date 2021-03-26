from flask import Flask, render_template, url_for, request, redirect, jsonify
import smtplib, ssl
import os

app = Flask(__name__)

@app.route('/')
def render_page():
    return render_template('email_contact.html')

@app.route('/feedback', methods = ['POST'])
def send_feedback():
    sender_email = os.environ.get('gmail_password')
    receiver_email = 'olleksii112@gmail.com'
    password = os.environ.get('password_gmail')
    if request.method == 'POST':
        with smtplib.SMTP('smtp.gmail.com',587) as server:

            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login(sender_email,password)
            subject = request.form['subject_feedback']
            body = request.form['content']
            email_feedback = request.form['email_feedback']
            name_feedback = request.form['Name']
            msg = f'Subject: {subject}\n\n{email_feedback}\n\n{name_feedback}\n\n{body}'.encode('utf-8')

            server.sendmail(sender_email,receiver_email,msg)
    return redirect(url_for('render_page'))

if __name__== '__main__':
    app.run(debug=True)