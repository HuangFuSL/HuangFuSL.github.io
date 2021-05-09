from __future__ import annotations
from xml.etree import ElementTree


def latex_image(filename: str, alt: str = "", width: str | None = None, page: int | None = None):

    img = ElementTree.Element('img')
    if page is None:
        filename = "{0}.svg".format(filename[:-4])
    else:
        filename = "{0}-{1}.svg".format(filename[:-4])
    img.set('src', '../' + filename)
    img.set('alt', alt)
    img.set('class', 'latex')
    if width is not None:
        img.set('width', width)
    return ElementTree.tostring(img).decode()
