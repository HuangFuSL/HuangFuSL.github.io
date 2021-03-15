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
                    curPath, verbose=True, raise_on_error=True, optionflags=doctest.ELLIPSIS)


SOURCE_DIR = "."
HTML_DIR = os.path.join("..", "HuangFuSL.github.io")

COMMAND_LIST = {
    'build': 'mkdocs build -d built --no-directory-urls',
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
    subprocess.run(COMMAND_LIST['pull'], cwd=src)
    subprocess.run(COMMAND_LIST['build'], cwd=src)
    ret2 = subprocess.run(
        COMMAND_LIST['check'], text=True, capture_output=True, cwd=src)
    if 'nothing to commit' not in ret2.stdout:
        subprocess.run(COMMAND_LIST['add'], cwd=src)
        subprocess.run(
            COMMAND_LIST['commit'] % (
                "Update on " +
                time.strftime(
                    "%Y/%m/%d %H:%M:%S",
                    time.localtime(time.time())
                ),
            ),
            cwd=src
        )
        subprocess.run(COMMAND_LIST['push'], cwd=src)
    else:
        print("HTML files not updated.")
