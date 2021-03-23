import urllib.request, urllib.parse, urllib.error
import json
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/graylog/lost-access', methods=['POST'])

def lostaccess():
    jasminurl = 'http://smsgate.example.com:1401/send?%s'
    baseParams = {'username':'user', 'password':'pswd', 'from':'TEST', 'coding': '0'}
    phones = {'User1': 'Phone1', 'User2': 'Phone2', 'User3': 'Phone3'}

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

@app.route('/graylog/sms-error', methods=['POST'])

def smserror():
    jasminurl = 'http://smsgate.example.com:1401/send?%s'
    baseParams = {'username':'user', 'password':'pswd', 'from':'TEST', 'coding': '0'}
    phones = {'User1': 'Phone1', 'User2': 'Phone2', 'User3': 'Phone3'}

    def send(phone):
        baseParams['to'] = phone
        urllib.request.urlopen(jasminurl % urllib.parse.urlencode(baseParams)).read()

    baseParams['content'] = 'Error status in message in SMS Stream.'

    send(phones['User1'])
    send(phones['User2'])
    send(phones['User3'])

    return Response(status=200)
