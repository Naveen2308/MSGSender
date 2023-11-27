import pywhatkit
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/index.html')
def index1():
    return render_template("index.html")
@app.route("/about.html")
def about():
    return render_template("about.html")
@app.route("/contact.html")
def contact():
    return render_template("contact.html")
@app.route('/process', methods=['POST'])
def process():
    c = request.form.get("country")
    phn = request.form.get("num")
    msg = request.form.get("message")
    phn = c+phn
    # Check if the phone number is valid (you can implement your validation logic here)

    # Send a WhatsApp message with a 10-second delay
    try:
        pywhatkit.sendwhatmsg_instantly(phn,msg, 10)
        return render_template("index.html",info = "Message sent successfully")
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100, debug=False)