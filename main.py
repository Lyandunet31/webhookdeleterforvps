
    # app.py
from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

@app.route('/webhookspammer', methods=['GET', 'POST'])
def webhook_deleter():
    if request.method == 'POST':
        webhook_url = request.form['webhook_url']
        data = {
            "content" : "Webhook spammer powered by ez services",
            "username" : "Ez services on top"
            }
            while True:
                requests.post(webhook_url,data)
        if response.status_code == 204:
            return "Spamming...!"
        else:
            return "Failed to spam!"
    return '''
        <form action="/webhooksender" method="post">
            <input type="text" name="webhook_url" placeholder="Enter Discord Webhook URL">
            <button type="submit">Spam webhook</button>
        </form>
    '''
