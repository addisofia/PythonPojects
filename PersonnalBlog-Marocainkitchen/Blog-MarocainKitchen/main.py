from flask import Flask ,render_template,request
import requests
import smtplib
import os
from dotenv import load_dotenv




load_dotenv()

MYEMAIL=os.getenv("MYEMAIL")
MYPASSWORD=os.getenv("MYPASSWORD")

api_url="https://api.npoint.io/4a69316242ed018d4f92"
posts=requests.get(api_url).json()

app=Flask(__name__)
@app.route("/")
@app.route("/home")
def home():

    return render_template("index.html",all_posts=posts)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    request_post="none"
    for p in posts:
        p["id"] = int(p["id"])
        if p["id"]==post_id :
            request_post=p
    return render_template("post.html",post=request_post)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/contactForm',methods=["POST"])
def receive_data():
    if request.method=="POST":
        name = request.form.get("name")
        email = request.form.get("email")
        Tel = request.form.get("phone")
        subject=request.form.get("message")
        email_message = f"Subject: Contact:message from visitor Look & Cook website\n\n"
        email_message +=f"NAME :{name}\n EMAIL:{email}\n PHONE:{Tel}\n MESSAGE :{subject}"
        try:
             with smtplib.SMTP("smtp.gmail.com",587) as connection:
                 connection.starttls()
                 connection.login(user=MYEMAIL,password=MYPASSWORD)
                 connection.sendmail(from_addr=MYEMAIL,to_addrs=MYEMAIL,msg=email_message.encode("utf-8"))
             return f"Thanks {name} for your visit, Information send successfully!"
        except Exception as e:
             return f"could'nt send the message: {e}"


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__== "__main__":
    app.run(debug=True)