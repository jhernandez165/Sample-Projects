import requests

def get_request(event=None, context=None):
    r = requests.get("https://www.scriptchain.co")
    if r.status_code == 200:
        return "It was successful"
    else:
        return f"Failed with status code {r.status_code}"

print(get_request())
