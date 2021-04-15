import urllib.request
import bs4
import zipfile
import os

_BASE = 'https://github.com'
_URL = 'https://github.com/twbs/icons/releases/latest/'


def _get_link():
    resp = urllib.request.urlopen(_URL)
    content = resp.read().decode(encoding="utf-8")
    docTree = bs4.BeautifulSoup(content)
    link = docTree.find_all('a', rel="nofollow")[0]['href']
    return _BASE + link


def _download(url):
    with urllib.request.urlopen(url) as f, open('temp.zip', 'wb') as d:
        d.write(f.read())
    archive = zipfile.ZipFile('temp.zip')
    for item in archive.namelist():
        if item[-1] == "/" and item.count('/') == 1:
            dirname = item[:-1]
        elif item[-3:] == "svg":
            archive.extract(item, os.path.join('overrides', '.icons'))

    os.rename(
        os.path.join('overrides', '.icons', dirname),
        os.path.join('overrides', '.icons', 'bootstrap')
    )

    archive.close()
    os.remove('temp.zip')


def get_icon():
    _download(_get_link())


if __name__ == "__main__":
    _download(_get_link())
