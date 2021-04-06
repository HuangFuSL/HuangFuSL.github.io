'''
Convert.py - convert latex markedups to SVG

This is a Python wrapper for xelatex and dvisvgm, so make sure you have these
components installed and correctly configured.

Usage:

Here is a latex document whose name is `test.tex`

```tex
\documentclass{article}
\begin{document}
    \pagestyle{empty}
    \begin{tabular}{|c|c|c|}
        \hline 2&9&4\\
        \hline 7&5&3\\
        \hline 6&1&8\\
        \hline
    \end{tabular}
\end{document}
```

If you want to embed this document in markdown, you should import it as an SVG
image.

![This is an test image](test.svg)

Remember to add `\pagestyle{empty}` in the document if it's used for 
demonstrating purposes and you don't want the page numbers to be rendered.

Please ensure that the tex document SHOULD NOT exceed one page, otherwise the
filename of the SVG file would change. The filename is in the following format:
(page index starts from 1)

```
[tex filename]-[page index].svg
```

For example, the SVG file corresponds to the first page of `test.tex` is
`test-1.svg`. You should match each page manually.

Execute the script in the root directory, and the script will scan the whold
project recursively, convert all `.tex` files to `.svg` files.
'''

import os
import subprocess


XELATEX_CMD = [
    'xelatex',
    '-synctex=1',
    '-interaction=nonstopmode',
    '-file-line-error', 
    '-no-pdf'
]
DVISVGM_CMD = ['dvisvgm', '--page=1-', '--scale=2', '--font-format=woff']


def _cleanup(filename: str):
    remove_ext = ['pdf', 'aux', 'synctex.gz', 'xdv', 'log']
    for ext in remove_ext:
        try:
            to_remove = filename[:-3] + ext
            if os.path.exists(to_remove):
                os.remove(to_remove)
        except:
            pass

def _conversion(filename: str, cwd: str = '.'):
    '''
    Execute the following command to convert the file:

    ```bash
    xelatex -synctex=1 -interaction=nonstopmode -file-line-error -no-pdf input.tex
    dvisvgm --page=1- --scale=2 --font-format=woff input.xdv
    ```
    '''
    print('Converting: ', filename)
    dvi_name = filename[:-3] + 'xdv'
    subprocess.run(XELATEX_CMD + [filename], cwd=cwd)
    subprocess.run(DVISVGM_CMD + [dvi_name], cwd=cwd)
    _cleanup(filename)


def tex2svg(cwd: str = '.'):
    '''
    Convert the `.tex` file recursively.
    '''
    for _ in os.listdir(cwd):
        curPath = os.path.join(cwd, _)
        if os.path.isdir(curPath):
            tex2svg(curPath)
        elif os.path.isfile(curPath):
            if _.split('.')[-1] == 'tex':
                _conversion(curPath, cwd)


if __name__ == '__main__':
    tex2svg(os.getcwd())
