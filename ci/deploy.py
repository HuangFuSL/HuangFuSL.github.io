import argparse
import os
import subprocess
import sys
import time

import bootstrap
import convert
import tsinghua

parser = argparse.ArgumentParser()
parser.add_argument("--dry-run", action="store_true", help="Do not actually deploy")


def apply_token(id: str, token: str):
    new = os.path.join("overrides", "main.html")
    old = os.path.join("overrides", "_main.html")
    _output = open(new, "w", encoding='utf-8')
    _input = open(old, "r", encoding="utf-8")
    for line in _input.readlines():
        if "clientSecret" in line:
            line = line % (token, )
        if "clientID" in line:
            line = line % (id, )
        _output.write(line)
    print("Token applied to {}".format(new))
    _input.close()
    _output.close()


SOURCE_DIR = "."

if __name__ == "__main__":
    ns = parser.parse_args()
    dry_run = ns.dry_run
    os.chdir(SOURCE_DIR)
    if ("CI" not in os.environ or not os.environ["CI"]) and not dry_run:
        print("This script is designed for CI execution.")
        sys.exit()
    if "GITALK_SECRET" in os.environ and "GITALK_ID" in os.environ:
        apply_token(os.environ["GITALK_ID"], os.environ["GITALK_SECRET"])

    src = os.getcwd()
    convert.tex2svg(src)
    bootstrap.get_icon()
    tsinghua.build_icon()
    msg = "Update on " + \
        time.strftime("%Y/%m/%d %H:%M:%S", time.gmtime(time.time() + 3600 * 8))
    subprocess.run(
        'mkdocs build -d build',
        cwd=src, shell=True
    )
    if not dry_run:
        subprocess.run(
            'mkdocs gh-deploy -d build --message "%s"' % (msg, ),
            cwd=src, shell=True
        )
    else:
        print("Dry run, not deploying.")
