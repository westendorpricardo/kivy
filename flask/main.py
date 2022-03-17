from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/time')
def getTime():
    time = datetime.now()
    return "RPI3 date and time: " + str(time)

app.run(host='0.0.0.0', port=8090)