import argparse
import os
import subprocess
import sys
import time

import convert
import tsinghua

parser = argparse.ArgumentParser()
parser.add_argument('--dry-run', action='store_true')
parser.add_argument('--python', default='python3')


SOURCE_DIR = '.'

if __name__ == '__main__':
    ns = parser.parse_args()
    dry_run = ns.dry_run
    python = ns.python
    os.chdir(SOURCE_DIR)
    if ('CI' not in os.environ or not os.environ['CI']) and not dry_run:
        print('This script is designed for CI execution.')
        sys.exit()

    src = os.getcwd()
    convert.tex2svg(src)
    tsinghua.build_icon()
    msg = 'Update on ' + \
        time.strftime('%Y/%m/%d %H:%M:%S', time.gmtime(time.time() + 3600 * 8))
    subprocess.run(
        f'{python} -m mkdocs build -d build',
        cwd=src, shell=True, check=True
    )
    if not dry_run:
        subprocess.run(
            f'{python} -m mkdocs gh-deploy -d build --message "{msg}"',
            cwd=src, shell=True, check=True
        )
    else:
        subprocess.run(
            f'{python} -m mkdocs build -d build --clean',
            cwd=src, shell=True, check=True
        )
