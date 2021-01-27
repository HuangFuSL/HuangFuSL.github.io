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
            if _[-2:] == "md":
                doctest.testfile(curPath, verbose=True, raise_on_error=True)


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
    ret = subprocess.run(
        COMMAND_LIST['check'], text=True, capture_output=True, cwd=src)
    if 'clean' not in ret.stdout:
        subprocess.run(COMMAND_LIST['add'], cwd=os.getcwd())
        subprocess.run(
            COMMAND_LIST['commit'] % (
                "Update on " +
                time.strftime(
                    "%Y/%m/%d %H:%M:%S",
                    time.localtime(time.time())
                ),
            ),
            cwd=os.getcwd()
        )
        subprocess.run(COMMAND_LIST['push'], cwd=src)
        os.chdir(HTML_DIR)
    else:
        print("Source not updated.")
    subprocess.run(COMMAND_LIST['pull'], cwd=os.getcwd())
    subprocess.run(COMMAND_LIST['build'], cwd=src)
    ret2 = subprocess.run(
        COMMAND_LIST['check'], text=True, capture_output=True, cwd=os.getcwd())
    if 'clean' not in ret2.stdout:
        subprocess.run(COMMAND_LIST['add'], cwd=os.getcwd())
        subprocess.run(
            COMMAND_LIST['commit'] % (
                "Update on " +
                time.strftime(
                    "%Y/%m/%d %H:%M:%S",
                    time.localtime(time.time())
                ),
            ),
            cwd=os.getcwd()
        )
        subprocess.run(COMMAND_LIST['push'], cwd=os.getcwd())
    else:
        print("HTML files not updated.")
