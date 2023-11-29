from __future__ import annotations

import itertools
import json
from typing import Any, Dict, List

from mkdocs_macros import plugin

_page_meta_collection = {}
_page_meta_original = {}


def collect_meta(env) -> None:
    if not _page_meta_original:
        load_meta()
    _page_meta_collection[env.page.url] = {
        'title': env.page.title,
        'meta': env.page.meta,
        'url': env.page.url,
        'file': env.page.file.src_uri,
    }


def load_meta() -> None:
    global _page_meta_original
    try:
        with open('meta.json', 'r', encoding='utf-8') as file:
            _page_meta_original = json.load(file)
    except:
        _page_meta_original = {}
    if len(_page_meta_original):
        print(f'Loaded metadata for {len(_page_meta_original)} pages')


def write_meta(_: plugin.MacrosPlugin) -> None:
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
    pages: List[Dict[str, Any]] = [
        {
            'url': v['file'],
            'title': f"[{v['title']}]({v['file']})",
            'sub_title': v['meta']['git_creation_date_localized_raw_iso_date'], # type: ignore
            'content': v['meta'].get('description', '')  # type: ignore
        }
        for v in _page_meta_original.values()
        if criteria(v)
    ]
    pages.sort(key=lambda _: _['sub_title'], reverse=True)
    return json.dumps(pages[:topk])

def build_recent(topk: int) -> str:
    pages: List[Dict[str, Any]] = [
        {
            'url': v['file'],
            'title': f"[{v['title']}]({v['file']})",
            'sub_title': v['meta']['revision_date'],  # type: ignore
            'content': v['meta'].get('summary', '')  # type: ignore
        }
        for v in _page_meta_original.values()
        if criteria(v)
    ]
    pages.sort(key=lambda _: _['sub_title'], reverse=True)
    grouped = [
        f"* {k}：{'，'.join([_['title'] for _ in v])}"
        for k, v in itertools.groupby(pages, lambda _: _['sub_title'])
    ][:topk]
    return '\n'.join(grouped)

def build_todo() -> str:
    pages: List[Dict[str, Any]] = [
        {
            'url': v['file'],
            'title': f"[{v['title']}]({v['file']})"
        }
        for v in _page_meta_original.values()
        if criteria(v) and (v['meta'].get('todo', False))
    ]
    pages.sort(key=lambda _: _['title'], reverse=True)
    if pages:
        return '\n'.join([f"* {page['title']}" for page in pages])
    return 'TODO list is clear!'

def filter_pages(category: str) -> List[Dict[str, str | Dict[str, str]]]:

    def helper(_):
        return 'category' in _['meta'] and _['meta']['category'] == category
    return [item for item in _page_meta_original.values() if helper(item)]


def get_meta_original() -> Dict[str, Dict[str, str | Dict[str, str]]]:
    return _page_meta_original


def set_meta_original(o: Dict[str, Dict[str, str | Dict[str, str]]]):
    global _page_meta_original
    _page_meta_original = o


def get_meta_collection() -> Dict[str, Dict[str, str | Dict[str, str]]]:
    return _page_meta_collection


def set_meta_collection(o: Dict[str, Dict[str, str | Dict[str, str]]]):
    global _page_meta_collection
    _page_meta_collection = o
