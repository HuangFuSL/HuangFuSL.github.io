import json
from typing import Any, Dict, Optional


def load_tech_tree() -> Dict[str, Dict[str, Any]]:
    with open('data/aoe2/techtree.json') as f:
        tech_tree = json.load(f)
    return tech_tree


def load_img_urls() -> Dict[str, Dict[str, Dict[str, str]]]:
    with open('data/aoe2/imgs.json') as f:
        return json.load(f)


img_urls = load_img_urls()
tech_tree = load_tech_tree()


def get_url(name: str, type_: str, available: bool) -> str:
    return img_urls[type_][name]["1" if available else "0"]


def build_row(
    tree_row: Dict[str, Optional[bool]],
    building: Optional[str] = None, available: bool = True
):
    content = []
    if building is not None:
        img = get_url(building, 'buildings', available)
        content.append(f'![{building}]({img}) @span @class="aoe2"')
    else:
        content.append(' ')

    for k, v in tree_row.items():
        if v is None:
            if content[-1] == '→':
                content[-1] = '&emsp;'
            content.append('&emsp;')
            content.append('&emsp;')
            continue

        isolate = k.startswith('~')
        k = k[1:] if isolate else k
        if isolate:
            content[-1] = '&emsp;'

        img = get_url(k, 'items', v)
        content.append(f'![{k}]({img}) @class="aoe2"')
        content.append('→')
    content.pop()
    return f"|{'|'.join(content)}|"


def build_header():
    content = ['建筑']
    for k, v in img_urls['Ages'].items():
        content.append(f'![{k}]({v}) @class="aoe2"')
        content.append('→')
    content[-1] = '&emsp;'
    content.append('&emsp;')
    return f"|{'|'.join(content)}|"


def get_midrule():
    content = [':-:'] * 10
    return f"|{'|'.join(content)}|"


def build_building_tree(
    civ: str, building: str
):
    result = []
    content = tech_tree[civ][building]
    available = content['available']
    items = content.get('items', [])
    first_row = building
    for u in items:
        result.append(build_row(u, first_row, available))
        first_row = None

    return '\n'.join(result)


def build_tech_tree(civ: str):
    result = []
    result.append(build_header())
    result.append(get_midrule())
    for _ in tech_tree[civ].keys():
        result.append(build_building_tree(civ, _))

    return '\n'.join(result)
