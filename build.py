import time
import os
import subprocess
import doctest
import sys


def check_doc(cwd: str):
    for _ in os.listdir(cwd):
        curPath = os.path.join(cwd, _)
        if os.path.isdir(curPath):
            check_doc(curPath)
        elif os.path.isfile(curPath):
            if _[-2:] == "md" and "pyguide" not in _:
                doctest.testfile(
                    curPath, verbose=True, optionflags=doctest.ELLIPSIS)

def apply_token(token: str):
    new = os.path.join("overrides", "main.html")
    old = os.path.join("overrides", "_main.html")
    _output = open(new, "w", encoding='utf-8')
    _input = open(old, "r", encoding="utf-8")
    for line in _input.readlines():
        if "clientSecret" in line:
            line = line % (token, )
        _output.write(line)
    _input.close()
    _output.close()
    

SOURCE_DIR = "."

if __name__ == "__main__":
    os.chdir(SOURCE_DIR)

    if "GITALK_SECRET" in os.environ:
        apply_token(os.environ["GITALK_SECRET"])

    try:
        check_doc(SOURCE_DIR)
    except:
        print("doctest failed")
        sys.exit(-1)

    # check the status of the source
    # if the working tree is clean,
    # no rebuild and commit required.
    src = os.getcwd()
    msg = "Update on " + \
        time.strftime("%Y/%m/%d %H:%M:%S", time.gmtime(time.time() + 3600 * 8))
    if len(sys.argv) > 1 and sys.argv[1] == "github-actions":
        subprocess.run(
            'mkdocs gh-deploy -d built --message "%s"' % (msg, ),
            cwd=src, shell=True
        )
    else:
        subprocess.run('git add --all'.split(), cwd=src)
        subprocess.run(
            ['git', 'commit', '-a', '--message=%s' % (msg, )],
            cwd=src
        )
        subprocess.run(
            'git push'.split(),
            cwd=src
        )
