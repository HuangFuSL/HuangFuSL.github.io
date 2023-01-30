from mkdocs_macros import plugin

from . import aoe2, latex, leetcode, metadata, network

on_pre_page_macros = metadata.collect_meta
on_post_build = metadata.write_meta


def define_env(env: plugin.MacrosPlugin):
    env.macro(metadata.filter_pages)
    env.macro(leetcode.display_difficulty)
    env.macro(leetcode.build_tag_mapping)
    env.macro(leetcode.get_md_table)
    env.macro(leetcode.get_whole_table)
    env.macro(latex.latex_image)
    env.macro(network.remote_content)
    env.macro(network.wechat_post)
    env.macro(metadata.build_timeline)
    env.macro(metadata.build_recent)
    env.macro(aoe2.build_tech_tree)
    env.filter(len)