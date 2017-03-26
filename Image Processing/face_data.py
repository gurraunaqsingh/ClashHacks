import cognitive_face as CF
import requests
import http.client, urllib, base64,json

def face_response(link):
	KEY = '2dd67b1bada44b18808bcc43fa3a1381'
	CF.Key.set(KEY)
	headers={
	    # Request headers
	    'Content-Type': 'application/json',
	    'Ocp-Apim-Subscription-Key': '76dd0d9c34764dc3bc2d8419c769db29',
	}
	params = urllib.parse.urlencode({
	})
	try:
		url={"url": link}
		conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
		conn.request("POST", "/emotion/v1.0/recognize?%s" % params, json.dumps(url), headers)
		response = conn.getresponse()
		data = response.read()
		return(data)
		conn.close()
	except Exception as e:
		print("[Errno {0}] {1}".format(e.errno, e.strerror))
