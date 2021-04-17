import json

from .leetcode import *
from .metadata import *


on_pre_page_macros = collect_meta
on_post_build = write_meta
    

def define_env(env):
    env.macro(filterPages)
    env.macro(display_difficulty)
    env.macro(build_tag_mapping)
    env.macro(get_md_table)
