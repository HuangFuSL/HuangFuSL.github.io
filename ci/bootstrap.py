import urllib.request
import zipfile
import os

_VER = '1.9.1'
_URL = 'https://github.com/twbs/icons/releases/download' \
    f'/v{_VER}/bootstrap-icons-{_VER}.zip'


def _download(url):
    with urllib.request.urlopen(url) as f, open('temp.zip', 'wb') as d:
        d.write(f.read())
    with zipfile.ZipFile('temp.zip') as archive:
        dirname = ''
        for item in archive.namelist():
            if item[-1] == '/' and item.count('/') == 1:
                dirname = item[:-1]
            elif item[-3:] == 'svg':
                archive.extract(item, os.path.join('overrides', '.icons'))

        if not os.path.exists(os.path.join('overrides', '.icons', 'bootstrap')):
            os.rename(
                os.path.join('overrides', '.icons', dirname),
                os.path.join('overrides', '.icons', 'bootstrap')
            )

    os.remove('temp.zip')


def get_icon():
    _download(_URL)


if __name__ == '__main__':
    _download(_URL)
