import urllib.request, urllib.parse, urllib.error
import json
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/graylog', methods=['POST'])

def respond():
    jasminurl = 'http://example.com:1401/send?%s'
    baseParams = {'username':'jasmin', 'password':'passwd', 'from':'sys', 'coding': '0'}
    phones = {'User1': '123', 'User2': '321', 'User3': '231'}

    def send(phone):
        baseParams['to'] = phone
        urllib.request.urlopen(jasminurl % urllib.parse.urlencode(baseParams)).read()

    data = json.loads(request.data)
    print(data)
    try:
        baseParams['content'] = data['check_result']['matching_messages'][0]['fields']['logsource'] +" "+ data['stream']['alert_conditions'][0]['title'] +" "+ data['check_result']['matching_messages'][0]['fields']['lun']
    except:
        print("Error parsing message.")
        return Response(status=200)

    print(baseParams['content'])

    send(phones['User1'])
    send(phones['User2'])
    send(phones['User3'])

    return Response(status=200)
