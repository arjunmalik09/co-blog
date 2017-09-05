import httplib, urllib, base64
from json import JSONEncoder
from json import JSONDecoder

def get_tags(text="My name is Robin Chawla. I study in Computer Scince and Engineering in Banaras Hindu Unversity. I cracked IIT-JEE with rank 912 in year 2014. I was very happy at that time"):
    body={
      "documents": [
        {
          "id": "abcd",
          "text": text
        }
      ]
    }

    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '183f71b817464e95a22f669bcfad216e',
    }

    strng=JSONEncoder().encode(body)

    params = urllib.urlencode({
    })
    L = []
    try:
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/text/analytics/v2.0/keyPhrases?%s" % params, strng, headers)
        response = conn.getresponse()
        data = response.read()
        
       # print(data)

        newdict=JSONDecoder().decode(data)
       # print(newdict)
        L=newdict["documents"][0]["keyPhrases"]
        
        conn.close()
    except Exception as e:
        print("Internet Connection Error")
    return L

L = get_tags()
print L
