from flask import Flask, url_for
from markupsafe import escape
from flask import render_template, request, flash, redirect
from utils.email import EmailService

app = Flask(__name__)
app.config.update(
    SECRET_KEY=b'_5#y3D"F4Q8z\n\xec]/'
)

@app.route('/')
def index():
    flash(u'Welcome to Baba Iron and Cement Store', 'info')
    return render_template('index.html', )

@app.route('/index.html')
def index_x():
    return render_template('index.html', )

@app.route('/about.html')
def about():
    return render_template('about.html', )


@app.route('/contact.html', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "")
        email = request.form.get("email", "")
        phone = request.form.get("phone", "")
        message = request.form.get("message", "")
        message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
        EmailService(app).send_mail(email, name, message)
        flash(u'Your Query is submitted', 'success')
        return redirect("/index.html")

    return render_template('contact.html', )

@app.route('/time.html')
def time():
    return render_template('time.html', )

@app.route('/coaching.html')
def coaching():
    return render_template('coaching.html', )

@app.route('/login')
def login():
    return 'login'

@app.route('/email_raw')
def email_raw():
    return render_template('mail/contact_us_customer.html')
