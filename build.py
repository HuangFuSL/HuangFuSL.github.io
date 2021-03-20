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


SOURCE_DIR = "."
HTML_DIR = os.path.join("..", "HuangFuSL.github.io")

COMMAND_LIST = {
    'build': 'mkdocs build -d %s --no-directory-urls' % (HTML_DIR),
    'check': 'git status',
    'push': 'git push',
    'pull': 'git pull',
    'add': 'git add --all',
    'commit': 'git commit -a --message="%s"'
}

if __name__ == "__main__":
    os.chdir(SOURCE_DIR)

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
