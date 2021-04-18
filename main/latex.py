from __future__ import annotations


def latex_image(filename: str, alt: str = "", page: int | None = None):
    if page is None:
        return "![{1}]({0}.svg)".format(filename[:-4], alt)
    else:
        return "![{2}]({0}-{1}.svg)".format(filename[:-4], page, alt)
