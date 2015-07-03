import os
import suds_marketo
import urllib3
from flask import Flask, request, json


from flask.ext import restful
from flask.ext.jsonpify import jsonify

app = Flask(__name__)
api = restful.Api(app)

class merge(restful.Resource):
    def get(self, ID):
        #Establish Connection to OpenTable Marketo Endpoint
        client = suds_marketo.Client(soap_endpoint='',
                                     user_id='6282468SDF7530E8A604131D1',
                                     encryption_key='53351376551375325D53300EE88AA66124EF4113492BE69SSD')

        NewContactFromSFDC = str(ID)
        #get the leads from Marketo
        lead = client.get_lead_IDNUM(NewContactFromSFDC)
        for i in range(0,len(lead.leadRecordList.leadRecord[0].leadAttributeList[0])):
            if 'mKTOLeadID' == lead.leadRecordList.leadRecord[0].leadAttributeList[0][i].attrName:
                originalmarketoid = lead.leadRecordList.leadRecord[0].leadAttributeList[0][i].attrValue
        try:
            #Try and merge leads if they both exist in marketo.  One will be the new SFDC contact
            #One will be the marketo lead that was a lead before it was an SFDC contact.
            client.merge_leads(NewContactFromSFDC,originalmarketoid)
        except:
            pass
        return None

api.add_resource(merge, '/<int:ID>')

if __name__ == '__main__':
    #app.run(debug=True)
    #for debugging
    print 'lol'
