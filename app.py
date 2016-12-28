import os
from bottle import route, run
import requests

@route('/send')
def send():
    response = requests.post(
        'https://notify-api.line.me/api/notify',
        {'message':'test'},
        headers={'Authorization': 'Bearer PNjKHTsdryx3oPkSlB5Tl3LzOBB0oWsVxXeN8Bd5XBF', 'Content-Type': 'application/x-www-form-urlencoded'})

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))