import requests
import lxml
import lxml.html

HEADERS = {
    'User-Agent': 'Mozilla/5.0 '\
        '(Windows NT 10.0; Win64; x64) '\
        'AppleWebKit/537.36 (KHTML, like Gecko) '\
        'Chrome/70.0.3538.77 Safari/537.36',
}

def remote_content(url):
    try:
        print('Downloading content from:', url)
        response = requests.get(url, headers=HEADERS, timeout=5)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except:
        return None

