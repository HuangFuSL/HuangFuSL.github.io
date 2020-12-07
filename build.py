import time
import os
import subprocess

SOURCE_DIR = r"C:\Users\huang\Documents\GitHub\BlogSource"
HTML_DIR = os.path.join("..", "HuangFuSL.github.io")

COMMAND_LIST = {
    'build': 'mkdocs build -d %s --no-directory-urls' % (HTML_DIR),
    'check': 'git status',
    'push': 'git push',
    'add': 'git add --all',
    'commit': 'git commit -a --message="%s"'
}

if __name__ == "__main__":
    os.chdir(SOURCE_DIR)

    # check the status of the source
    # if the working tree is clean,
    # no rebuild and commit required.
    ret = subprocess.run(
        COMMAND_LIST['check'], text=True, capture_output=True, cwd=os.getcwd())
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
        subprocess.run(COMMAND_LIST['push'], cwd=os.getcwd())
        subprocess.run(COMMAND_LIST['build'], cwd=os.getcwd())
        os.chdir(HTML_DIR)
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
    else:
        print("Source not updated.")
