from . import leetcode
from . import metadata
from . import latex


on_pre_page_macros = metadata.collect_meta
on_post_build = metadata.write_meta


def define_env(env):
    env.macro(metadata.filterPages)
    env.macro(leetcode.display_difficulty)
    env.macro(leetcode.build_tag_mapping)
    env.macro(leetcode.get_md_table)
    env.macro(latex.latex_image)
    env.filter(len)
