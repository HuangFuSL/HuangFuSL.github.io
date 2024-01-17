from __future__ import annotations

def read_code_from_file(file_name: str, language: str | None = None) -> str:
    ''' Read from file, return a link and code block '''
    if language is None:
        language = file_name.split('.')[-1]
    file_url = file_name.removeprefix('docs')
    suffix_mapping = { 'py': 'python', 'rs': 'rust' }
    link = f'[:bootstrap-cloud-download: Download source code]({file_url})\n\n'
    code_block_prefix = f'```{suffix_mapping.get(language, str())}\n'
    with open(file_name, 'r') as f:
        code_block_body = f.read()
    code_block_suffix = '\n```'
    return link + code_block_prefix + code_block_body + code_block_suffix
