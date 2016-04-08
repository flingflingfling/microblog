#coding=utf-8
#copy from mega-flask

try:
    import httplib
except ImportError:
    import http.client as httplib
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

import json
from flask.ext.babel import gettext
from config import MS_TRANSLATOR_CLIENT_ID, MS_TRANSLATOR_CLIENT_SECRET

def microsoft_translate(text, sourceLang, destLang):
    if MS_TRANSLATOR_CLIENT_ID == '' or MS_TRANSLATOR_CLIENT_SECRET == '':
        return gettext('error: translation service not configured.')
    try:
    #get access token
        params = urlencode({
                'client_id':MS_TRANSLATOR_CLIENT_ID,
                'client_secret':MS_TRANSLATOR_CLIENT_SECRET,
                'scope':'http://api.microsoft_translate.com',
                'grant_type':'client_credentials'})
        conn = httplib.HTTPSConnection("datamarket.accesscontrol.windows.net")
        conn.request('POST','/v2/OAuth2-13', params)
        response = json.loads(conn.getrespose().read())
        token = response[u'access_token']

        #translate
        conn = httplib.HTTPConnection('api.microsofttranslator.com')
        params = {'appId': 'Bearer ' + token,
                  'from': sourceLang,
                  'to': destLang,
                  'text': text.encode("utf-8")}
        conn.request("GET", '/V2/Ajax.svc/Translate?' + urlencode(params))
        response = json.loads("{\"response\":" + conn.getresponse().read().decode('utf-8') + "}")
        return response["response"]
    except:
        return gettext('Error: Unexpected error.')

