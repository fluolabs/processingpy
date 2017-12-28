import urllib.request, json 

def getJSON(id):
    filepath = "https://fluolabs.com/userwords/" + id + ".json"
    with urllib.request.urlopen(filepath) as url:
        data = json.loads(url.read().decode())
    return(data)
