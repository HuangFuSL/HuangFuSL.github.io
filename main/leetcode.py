from __future__ import annotations

from typing import List


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
    col_names: List[str] = ['题目'] * 4,
    col_align: List[str] | str | None = [':-'] * 4
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

    def get_difficulty(diff):
        a, b = ':material-star:', ':material-star-outline:'
        return {
            '简单': a + b * 2,
            '中等': a * 2 + b,
            '困难': a * 3,
        }[diff]

    def get_md_links(page):
        stars = get_difficulty(page['meta']['difficulty'])
        return '[{1}{0[title]}](/{0[url]})'.format(page, stars)

    def indent_lines(indent, seq):
        for line in seq:
            yield ' ' * indent + line

    def key(_):
        return int(_['title'].split(".", 1)[0])

    ret = [
        joiner(col_names),
        joiner(col_align)
    ]

    iterator = iter(sorted(pages, key=key))
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
