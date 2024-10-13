# app.py
from flask import Flask, request, render_template_string
import paramiko

app = Flask(__name__)

@app.route('/control', methods=['GET', 'POST'])
def control_vps():
    if request.method == 'POST':
        hostname = "82.112.242.179"
        username = "root"
        password = request.form['password']
        command = request.form['command']
        output = execute_command(hostname, username, password, command)
        return f"<pre>{output}</pre>"
    return '''
        <form action="/control" method="post">
            <input type="password" name="password" placeholder="Enter VPS Password"><br>
            <input type="text" name="command" placeholder="Enter Command"><br>
            <button type="submit">Execute Command</button>
        </form>
    '''

def execute_command(hostname, username, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname, username=username, password=password)
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode() + stderr.read().decode()
        client.close()
        return output
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
