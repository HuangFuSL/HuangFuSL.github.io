from __future__ import annotations

import json
from typing import Any, Dict, List

from mkdocs_macros import plugin

_page_meta_collection = {}
_page_meta_original = {}


def collect_meta(env: plugin.MacrosPlugin) -> None:
    global _page_meta_original
    global _page_meta_collection
    if not _page_meta_original:
        load_meta()
    _page_meta_collection[env.page.url] = {
        'title': env.page.title,
        'meta': env.page.meta,
        'url': env.page.url
    }


def load_meta() -> None:
    global _page_meta_original
    try:
        with open('meta.json', 'r', encoding='utf-8') as file:
            _page_meta_original = json.load(file)
    except:
        _page_meta_original = {}
    print(f'Loaded metadata for {len(_page_meta_original)} pages')


def write_meta(_: plugin.MacrosPlugin) -> None:
    global _page_meta_collection
    global _page_meta_original
    if _page_meta_original != _page_meta_collection:
        with open('meta.json', 'w', encoding='utf-8') as file:
            json.dump(_page_meta_collection, file)


def criteria(v: Dict[str, Any]):
    ignore_titles = {'目录'}
    if v['title'] in ignore_titles:
        return False
    if 'hide' in v['meta']:
        if set(v['meta']['hide']).intersection({'navigation', 'toc'}):
            return False
    return True


def build_timeline(topk: int) -> str:
    global _page_meta_original
    pages: List[Dict[str, Any]] = [
        {
            'url': v['url'],
            'title': f"[{v['title']}]({v['url']})",
            'sub_title': v['meta']['git_creation_date_localized_raw_iso_date'], # type: ignore
            'content': v['meta'].get('summary', '') # type: ignore
        }
        for v in _page_meta_original.values()
        if criteria(v)
    ]
    pages.sort(key=lambda _: _['sub_title'], reverse=True)
    return json.dumps(pages[:topk])

def build_recent(topk: int) -> str:
    global _page_meta_original
    pages: List[Dict[str, Any]] = [
        {
            'url': v['url'],
            'title': f"[{v['title']}]({v['url']})",
            'sub_title': v['meta']['revision_date'],  # type: ignore
            'content': v['meta'].get('summary', '')  # type: ignore
        }
        for v in _page_meta_original.values()
        if criteria(v)
    ]
    pages.sort(key=lambda _: _['sub_title'], reverse=True)
    return '\n'.join([
        f"* {page['sub_title']}：{page['title']}"
        for page in pages[:topk]
    ])


def filter_pages(category: str) -> List[Dict[str, str | Dict[str, str]]]:
    global _page_meta_original

    def helper(_):
        return 'category' in _['meta'] and _['meta']['category'] == category
    return [item for item in _page_meta_original.values() if helper(item)]


def get_meta_original() -> Dict[str, Dict[str, str | Dict[str, str]]]:
    global _page_meta_original
    return _page_meta_original


def set_meta_original(o: Dict[str, Dict[str, str | Dict[str, str]]]):
    global _page_meta_original
    _page_meta_original = o


def get_meta_collection() -> Dict[str, Dict[str, str | Dict[str, str]]]:
    global _page_meta_collection
    return _page_meta_collection


def set_meta_collection(o: Dict[str, Dict[str, str | Dict[str, str]]]):
    global _page_meta_collection
    _page_meta_collection = o
