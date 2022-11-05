import argparse
import os
import subprocess
import sys
import time

import bootstrap
import convert
import tsinghua

parser = argparse.ArgumentParser()
parser.add_argument('--dry-run', action='store_true')


SOURCE_DIR = '.'

if __name__ == '__main__':
    ns = parser.parse_args()
    dry_run = ns.dry_run
    os.chdir(SOURCE_DIR)
    if ('CI' not in os.environ or not os.environ['CI']) and not dry_run:
        print('This script is designed for CI execution.')
        sys.exit()

    src = os.getcwd()
    convert.tex2svg(src)
    bootstrap.get_icon()
    tsinghua.build_icon()
    msg = 'Update on ' + \
        time.strftime('%Y/%m/%d %H:%M:%S', time.gmtime(time.time() + 3600 * 8))
    subprocess.run(
        'mkdocs build -d build',
        cwd=src, shell=True, check=True
    )
    if not dry_run:
        subprocess.run(
            f'mkdocs gh-deploy -d build --message "{msg}"',
            cwd=src, shell=True, check=True
        )
    else:
        print('Dry run, not deploying.')
