import os
import urllib3
from flask import Flask, request, json

import clearbit
from slacker import Slacker

from flask.ext import restful
from flask.ext.jsonpify import jsonify

app = Flask(__name__)
api = restful.Api(app)

# set slack and clearbit from environ
clearbit.key = os.environ.get('CLEARBIT')
SLACK = os.environ.get('SLACK')
slack = Slacker(SLACK)

class postUserToSlack(restful.Resource):
    def get(self, email):
        # grab NewSignUp from request
        NewSignUp = str(email)

        # get the new sign up info from Clearbit
        NewSignUp = clearbit.Person.find(email=NewSignUp, stream=True)

        # format NewSignUp for Slack
        # This is how we like it at Vidfluent, but you can change it accordingly
        # if you don't want All the clearbit data
        fields = []
        for attribute, value in NewSignUp.iteritems():
            newfield = {}
            if isinstance(value, dict) and 'handle' in value:
                if value['handle'] != None:
                    for a, v in value.items():
                        newfield = {}
                        newfield['title'] = a
                        newfield['value'] = str(v)
                        newfield['short'] = True
                        fields.append(newfield)   
            else:
                newfield['title'] = attribute
                newfield['value'] = str(value)
                newfield['short'] = True
                fields.append(newfield)

        # Make Success Kid the Avatar
        avatar = 'http://assets-s3.usmagazine.com/uploads/assets/articles/85688-success-kid-meme-kidney-sick-father/1429037342_success-kid-meme-lg.jpg'
        if NewSignUp != None:
            NewSignUp = {
                        "FullName": NewSignUp['name']['givenName'] + ' ' + NewSignUp['name']['familyName'],
                        "gender": NewSignUp['gender'],
                        "email": email,
                        "site": NewSignUp['site']
                        }
            attachments = [
                            {
                                "fallback": "We got a new user!",

                                "color": "#e8426a",

                                "pretext": "We got a new user!",

                                "author_name": NewSignUp["FullName"],
                                "author_link": NewSignUp['site'],
                                "author_icon": avatar,

                                "fields": fields,
                            }
                           ]

        # Send a message to #newcustomer channel
        slack.chat.post_message('#newsignups', 'get stoked!', 'NewSignUp Bot', attachments=attachments, icon_url=avatar)
        return None

api.add_resource(postUserToSlack, '/<string:email>')

if __name__ == '__main__':
    app.run(debug=True)
    print 'Vidfluent is very neat!'