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
        time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time()))
    subprocess.run(
        'mkdocs gh-deploy -d built --message "%s" --no-directory-urls' % (msg, ),
        cwd=src
    )
    
