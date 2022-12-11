r'''
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

![This is a test image](test.svg)

Remember to add `\pagestyle{empty}` in the document if it's used for
demonstrating purposes and you don't want the page numbers to be rendered.

Please ensure that the tex document SHOULD NOT exceed one page, otherwise the
filename of the SVG file would change. The filename is in the following format:
(page index starts from 1)

```markdown
[tex filename]-[page index].svg
```

For example, the SVG file corresponds to the first page of `test.tex` is
`test-1.svg`. You should match each page manually.

Execute the script in the root directory, and the script will scan the whole
project recursively, convert all `.tex` files to `.svg` files.
'''

import os
import time
import subprocess
from typing import Tuple, Generator


XELATEX_CMD = [
    'xelatex',
    '-synctex=1',
    '-interaction=nonstopmode',
    '-file-line-error',
]

DVISVGM_CMD = [
    'dvisvgm',
    '--pdf',
    '--page=1-',
    '--font-format=woff',
    '--trace-all'
]
TLMGR_CMD = [
    'tlmgr',
    'install'
]

def _install_deps(pkg: str):
    exec_args = {
        'capture_output': True
    }
    subprocess.run(XELATEX_CMD + [pkg], check=True, **exec_args)


def _cleanup(filename: str):
    '''
    Clean up the pdf, aux, synctex.gz, xdv, log files as they are not needed.
    '''
    remove_ext = ['pdf', 'aux', 'synctex.gz', 'xdv', 'log']
    for ext in remove_ext:
        try:
            to_remove = filename[:-3] + ext
            if os.path.exists(to_remove):
                os.remove(to_remove)
        except FileNotFoundError:
            pass

def _conversion(arg: Tuple[str, str]):
    '''
    Execute the following command to convert the file:

    ```bash
    xelatex -synctex=1 -interaction=nonstopmode -file-line-error input.tex
    dvisvgm --page=1- --font-format=woff --trace-all input.pdf
    ```
    '''
    filename, cwd = arg
    start = time.time()

    dvi_name = filename[:-3] + 'pdf'
    exec_args = {
        'cwd': cwd,
        'capture_output': True
    }
    try:
        result = subprocess.run(
            XELATEX_CMD + [filename], check=True, **exec_args)
        result = subprocess.run(
            XELATEX_CMD + [filename], check=True, **exec_args)
        result = subprocess.run(
            DVISVGM_CMD + [dvi_name], check=True, **exec_args)
    except subprocess.CalledProcessError as e:
        print(e.stdout.decode('utf-8'))
        raise e

    end = time.time()
    print(f'{filename} converted in {end - start:.2f} seconds')
    _cleanup(filename)


def get_tex_path(cwd: str = '.') -> Generator[Tuple[str, str], None, None]:
    '''
    Convert the `.tex` file recursively.
    '''
    for _ in os.listdir(cwd):
        cur_path = os.path.join(cwd, _)
        if os.path.isdir(cur_path):
            yield from get_tex_path(cur_path)
        elif os.path.isfile(cur_path):
            if _.split('.')[-1] == 'tex':
                yield (cur_path, cwd)


def tex2svg(cwd: str = '.'):
    for i in get_tex_path(cwd):
        _conversion(i)

if __name__ == '__main__':
    with open('latex_packages.txt', 'r') as f:
        for pkg in f:
            _install_deps(pkg.strip())
    tex2svg(os.getcwd())
