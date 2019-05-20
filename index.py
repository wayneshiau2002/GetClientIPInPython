from flask import Flask
from flask import request
import requests
import socket

app = Flask(__name__)
@app.route("/")
def index():
    return "Your IP:" + getClientIP() + "    Remote IP:" + getRemoteIP() + " (Private IP: " + getPrivateIP() + ")"

def getClientIP():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    
    # Get the first IP, because this is correct end-user IP
    if ip.find(',') != -1:
        ipArray = ip.split(',')
        ip = ipArray[0]
    return ip

def getRemoteIP():
    remoteIP = requests.get('http://ip.42.pl/raw').text
    return remoteIP

def getPrivateIP():
    try: 
        host_name = socket.gethostname() 
        privateIP = socket.gethostbyname(host_name)
    except: 
        return "Unable to get Hostname and IP"
    return privateIP

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=True)



