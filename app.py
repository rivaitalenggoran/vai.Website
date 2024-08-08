from flask import Flask, render_template,request,jsonify
import requests


RASA_API_URL = "http://localhost:5005/webhooks/rest/webhook"
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home/home.html')

@app.route('/about')
def about():
    return render_template('about/about.html')

@app.route('/portofolio')
def portofolio():
    return render_template('portofolio/portofolio.html')

@app.route('/contact')
def contact():
    return render_template('contact/contact.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    user_message = request.json['message']
    print("User Message: ", user_message)

    #Send user message to Rasa and get bot's response
    rasa_response = requests.post(RASA_API_URL, json={'message':user_message})
    rasa_response_json = rasa_response.json()

    print("Rasa Response:",rasa_response_json)

    bot_response = rasa_response_json[0]['text'] if rasa_response_json else "Maaf, Saya tidak mengerti boskuh"

    return  jsonify({'response': bot_response})


if __name__ == '__main__':
    app.run(debug=True, port=3000)
