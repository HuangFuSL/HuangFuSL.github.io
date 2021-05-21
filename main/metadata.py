from __future__ import annotations

import json
from typing import Dict, List

import mkdocs_macros.plugin as plugin

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
        with open("meta.json", "r", encoding="utf-8") as file:
            _page_meta_original = json.load(file)
    except:
        _page_meta_original = {}
    print("Loaded metadata for {} pages".format(len(_page_meta_original)))


def write_meta(env: plugin.MacrosPlugin) -> None:
    global _page_meta_collection
    global _page_meta_original
    if _page_meta_original != _page_meta_collection:
        with open("meta.json", "w", encoding="utf-8") as file:
            json.dump(_page_meta_collection, file)


def filterPages(category: str) -> List[Dict[str, str | Dict[str, str]]]:
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
