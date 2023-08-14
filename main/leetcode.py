from __future__ import annotations

import csv
import operator
from typing import Iterable, Iterator, List, Optional

from . import util


def display_difficulty(diff):
    color = {
        '简单': 'green',
        '中等': 'orange',
        '困难': 'red'
    }
    return f'难度：<font color={color[diff]}>**{diff}**</font>'


def get_difficulty(diff):
    a, b = ':material-star:', ':material-star-outline:'
    return {
        '简单': a + b * 2,
        '中等': a * 2 + b,
        '困难': a * 3,
    }[diff]


def build_table(
    src: Iterable | Iterator,
    indent: int = 0,
    col_names: Optional[List[str]] = None,
    col_align: Optional[List[str] | str] = None
):
    if col_names is None:
        col_names = ['题目'] * 5
    if not isinstance(src, Iterator):
        src = iter(src)
    if col_align is None:
        col_align = [':-'] * len(col_names)
    elif isinstance(col_align, str):
        col_align = [col_align] * len(col_names)
    else:
        if len(col_names) != len(col_align):
            raise ValueError(
                f'List length mismatch, got {len(col_names)} and {len(col_align)}'
            )

    def joiner(_):
        return f'|{"|".join(_)}|'

    def indent_lines(indent, seq):
        for line in seq:
            yield ' ' * indent + line

    ret = [
        joiner(col_names),
        joiner(col_align)
    ]

    flag = True
    while flag:
        row = []
        for _ in col_names:
            try:
                link = next(src)
            except StopIteration:
                if not row:
                    flag = False
                link = ''
            row.append(link)
        ret.append(joiner(row))
    return '\n'.join(indent_lines(indent, ret))


def get_md_table(
    pages,
    indent: int = 0,
    col_names: Optional[List[str]] = None,
    col_align: Optional[List[str] | str] = None
):

    def get_md_links(page):
        stars = get_difficulty(page['meta']['difficulty'])
        return '[{1}{0[title]}](/{0[url]})'.format(page, stars)

    def key(_):
        return int(_['title'].split('.', 1)[0])

    iterator = map(get_md_links, sorted(pages, key=key))
    return build_table(iterator, indent, col_names, col_align)


def get_whole_table(
    pages,
    data: str = 'data/leetcode.csv',
    indent: int = 0,
    col_names: Optional[List[str]] = None,
    col_align: Optional[List[str] | str] = None
):
    with open(data, 'r', encoding='utf-8', newline='') as file:
        content = list(csv.DictReader(file))

    pages_dict = {int(_['title'].split('. ')[0]): _ for _ in pages}
    new_page = []
    for page in content:
        if int(page['编号']) in pages_dict:
            page['linked'] = True
            page['link'] = pages_dict[int(page['编号'])]['file']
            new_page.append(page)
    content = new_page

    content.sort(key=util.wrap(operator.itemgetter('编号'), int))

    def build_link(content):
        stars = get_difficulty(content['难度'])
        if content['linked']:
            return '[{1}{0[编号]}. {0[名称]}](/{0[link]})'.format(content, stars)
        else:
            return '{1}{0[编号]}. {0[名称]}'.format(content, stars)

    return build_table(map(build_link, content), indent, col_names, col_align)


def build_tag_mapping(pages):
    ret = {}
    for page in pages:
        for keywd in page['meta']['tags']:
            if keywd not in ret:
                ret[keywd] = []
            ret[keywd].append(page)

    def key(_):
        return len(_[1])

    return sorted(ret.items(), key=key, reverse=True)
