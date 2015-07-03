import os
import urllib3
from flask import Flask, request, json

import clearbit
from slacker import Slacker

clearbit.key = '1bd77da89e73be5b12278a80d2fc3ff2'
slack = Slacker('xoxp-4477022291-4457488502-7201309238-0be375')

from flask.ext import restful
from flask.ext.jsonpify import jsonify

app = Flask(__name__)
api = restful.Api(app)

class merge(restful.Resource):
    def get(self, email):
        # grab NewSignUp from request
        NewSignUp = str(email)
        print NewSignUp
        # get the leads from Marketo
        NewSignUp = clearbit.Person.find(email=NewSignUp, stream=True)
        if NewSignUp != None:
          print NewSignUp

        # Send a message to #newcustomer channel
        # slack.chat.post_message('#newsignups', 'New Customer Test from Python app!')
        return None

api.add_resource(merge, '/<string:email>')

if __name__ == '__main__':
    app.run(debug=True)
    #for debugging
    print 'lol'
