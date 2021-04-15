import urllib.request
import zipfile
import os

_URL = 'https://github.com/twbs/icons/releases/download/v1.4.1/bootstrap-icons-1.4.1.zip'


def _download(url):
    with urllib.request.urlopen(url) as f, open('temp.zip', 'wb') as d:
        d.write(f.read())
    archive = zipfile.ZipFile('temp.zip')
    for item in archive.namelist():
        if item[-1] == "/" and item.count('/') == 1:
            dirname = item[:-1]
        elif item[-3:] == "svg":
            archive.extract(item, os.path.join('overrides', '.icons'))

    if not os.path.exists(os.path.join('overrides', '.icons', 'bootstrap')):
        os.rename(
            os.path.join('overrides', '.icons', dirname),
            os.path.join('overrides', '.icons', 'bootstrap')
        )

    archive.close()
    os.remove('temp.zip')


def get_icon():
    _download(_URL)


if __name__ == "__main__":
    _download(_URL)
