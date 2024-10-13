# app.py
from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form action="/webhookdeleter" method="post">
            <input type="text" name="webhook_url" placeholder="Enter Discord Webhook URL">
            <button type="submit">Delete Webhook</button>
        </form>
    '''

@app.route('/webhookdeleter', methods=['POST'])
def webhook_deleter():
    webhook_url = request.form['webhook_url']
    response = requests.delete(webhook_url)
    if response.status_code == 204:
        return "Webhook deleted successfully!"
    else:
        return "Failed to delete webhook!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)