from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Samuel Raju P"  
    username = os.getenv("USER", "codespace")
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    top_output = subprocess.getoutput("top -b -n 1")

    return f"<p>Name: {name}</p>" \
           f"<p>Username: {username}</p>" \
           f"<p>Server Time: {server_time}</p>" \
           f"<p>Top output</p>" \
           f"<pre>{top_output}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
