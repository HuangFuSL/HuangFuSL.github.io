import mkdocs_linkcheck as lc
import os

if __name__ == '__main__':
    os.chdir('docs')
    lc.check_links('.', ext='.md', method='head', recurse=True)  # type: ignore
