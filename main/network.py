import requests

def remote_content(url):
    try:
        print("Downloading content from:", url)
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except:
        return None