import time
import os
import subprocess


if __name__ == "__main__":
    # check the status of the source
    # if the working tree is clean,
    # no rebuild and commit required.
    src = os.getcwd()
    msg = "Update on " + \
        time.strftime("%Y/%m/%d %H:%M:%S", time.gmtime(time.time() + 3600 * 8))
    subprocess.run('git add --all'.split(), cwd=src)
    subprocess.run(
        ['git', 'commit', '-a', '--message=%s' % (msg, )],
        cwd=src
    )
    subprocess.run(
        'git push'.split(),
        cwd=src
    )
