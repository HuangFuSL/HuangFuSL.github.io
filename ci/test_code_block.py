import os
import doctest

def check_doc(cwd: str):
    for _ in os.listdir(cwd):
        curPath = os.path.join(cwd, _)
        if os.path.isdir(curPath):
            check_doc(curPath)
        elif os.path.isfile(curPath):
            if _[-2:] == "md" and "pyguide" not in _:
                doctest.testfile(
                    curPath,
                    verbose=True, raise_on_error=True,
                    optionflags=doctest.ELLIPSIS
                )

if __name__ == "__main__":
    src = os.getcwd()
    check_doc(src)