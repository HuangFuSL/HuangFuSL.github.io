from __future__ import annotations
from xml.etree import ElementTree


def latex_image(
    filename: str, alt: str = '',
    width: str | None = None, page: int = 1
):

    img = ElementTree.Element('img')
    filename = f'{filename[:-4]}-{page}.svg'
    img.set('src', '../' + filename)
    img.set('alt', alt)
    img.set('class', 'latex')
    if width is not None:
        img.set('width', width)
    return ElementTree.tostring(img).decode()
