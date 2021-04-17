from __future__ import annotations

import json
from main.metadata import get_meta_original
from typing import List

from mkdocs.structure.nav import Link, Navigation, Page, Section

def display_difficulty(diff):
    color = {
        '简单': 'green',
        '中等': 'orange',
        '困难': 'red'
    }
    return '难度：<font color={0}>**{1}**</font>'.format(color[diff], diff)


def get_md_table(
    pages,
    indent: int = 0,
    col_names: List[str] = ['题目'] * 5,
    col_align: List[str] | str | None = [':-'] * 5
):
    if col_align is None:
        col_align = [':-'] * len(col_names)
    elif isinstance(col_align, str):
        col_align = [col_align] * len(col_names)
    else:
        if len(col_names) != len(col_align):
            raise ValueError("List length mismatch, got {} and {}"
                             .format(len(col_names), len(col_align)))

    def joiner(_):
        return "|{}|".format("|".join(_))

    def get_md_links(page):
        return '[{0[title]}](/{0[url]})'.format(page)

    def indent_lines(indent, seq):
        for line in seq:
            yield ' ' * indent + line

    ret = [
        joiner(col_names),
        joiner(col_align)
    ]

    iterator = iter(pages)
    flag = True
    while flag:
        row = []
        for i in col_names:
            try:
                link = get_md_links(next(iterator))
            except StopIteration:
                if not row:
                    flag = False
                link = ""
            finally:
                row.append(link)
        ret.append(joiner(row))
    return "\n".join(indent_lines(indent, ret))


def build_tag_mapping(pages):
    ret = {}
    for page in pages:
        for keywd in page['meta']['tags']:
            if keywd not in ret:
                ret[keywd] = []
            ret[keywd].append(page)
    return ret


def filterPages(category: str):
    page_meta_original = get_meta_original().values()
    def helper(_): return 'category' in _['meta'] and _[
        'meta']['category'] == category
    return [item for item in page_meta_original if helper(item)]
