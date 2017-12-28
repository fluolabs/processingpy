import urllib.request, json 
with urllib.request.urlopen("https://fluolabs.com/userwords/fluolabs.json") as url:
    data = json.loads(url.read().decode())
    print(data)
