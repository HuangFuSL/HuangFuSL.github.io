import mkdocs_linkcheck as lc

if __name__ == '__main__':
    lc.check_links('./docs', ext='.md', method='head', recurse=True)  # type: ignore
