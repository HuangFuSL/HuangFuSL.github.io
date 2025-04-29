from __future__ import annotations

from typing import Iterable, Iterator, List, Optional


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

    while True:
        row = []
        for _ in col_names:
            try:
                link = next(src)
            except StopIteration:
                link = ''
            row.append(link)
        if not ''.join(row):
            break
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
    indent: int = 0,
    col_names: Optional[List[str]] = None,
    col_align: Optional[List[str] | str] = None
):
    pages_list = [
        (int(page['title'].split('. ')[0]), page) for page in pages
    ]
    pages_list.sort(key=lambda x: x[0])

    links = []
    for _, content in pages_list:
        stars = get_difficulty(content['meta']['difficulty'])
        links.append('[{stars}{title}](/{url})'.format(
            stars=stars, **content
        ))

    return build_table(links, indent, col_names, col_align)


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
