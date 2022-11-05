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

def wechat_post(url):
    try:
        print('Downloading content from:', url)
        response = requests.get(url, headers=HEADERS, timeout=5)
        if response.status_code == 200:
            result = response.text
        else:
            return None

        document = lxml.html.fromstring(result)
        title = document.xpath('//*[@id="activity-name"]/text()')
        author = document.xpath('//*[@id="js_name"]/text()')

        return f'[{title[0].strip()}]({url}) by {author[0].strip()}'
    except:
        return None
