# from flask import Flask

# app = Flask(__name__)

# PORT = 4390


# @app.route('/')
# def homepage():
#     return "Howdy hacker!!!"


# if __name__ == '__main__':
#     app.run(debug=True, port=PORT)


#!/usr/bin/env python
# encoding: utf-8
import os
from bottle import run, post

from pdpyras import APISession
import requests
import pypd
from datetime import datetime, timedelta
import json
from urllib import parse as urlparse


@post('/hello')
# def hello():
#     return 'Hello World!'
def slack(event):
    message_from_slack = dict(urlparse.parse_qsl(event["body"]))
    response_url = message_from_slack["response_url"]
    user_email = message_from_slack["text"]
    message_for_slack = "*Request body _after_ decoding:*\n" + user_email

    response_json = {
        'attachments': [
                    {
                        'text': message_for_slack,
                        'callback_id': "slashcommand",
                        'actions': [
                            {
                                'name': 'slashcommand_bu',
                                'text': 'A Button',
                                'type': "button",
                                'value': 0
                            }
                        ]
                    }
        ]
    }

    return {
        'statusCode': 200,
        'body': json.dumps(response_json)
    }


if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    run(host='0.0.0.0', port=port)
