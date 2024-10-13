# app.py
from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

@app.route('/webhookdeleter', methods=['GET', 'POST'])
def webhook_deleter():
    if request.method == 'POST':
        webhook_url = request.form['webhook_url']
        response = requests.delete(webhook_url)
        if response.status_code == 204:
            return "Webhook deleted successfully!"
        else:
            return "Failed to delete webhook!"
    return '''
        <form action="/webhookdeleter" method="post">
            <input type="text" name="webhook_url" placeholder="Enter Discord Webhook URL">
            <button type="submit">Delete Webhook</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
