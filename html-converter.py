from bs4 import BeautifulSoup as bs
import re

css_1 = '<link rel="stylesheet" type="text/css" href="https://docs.python.org/3/_static/classic.css" />'
css_2 = '<link rel="stylesheet" type="text/css" href="https://docs.python.org/3/_static/basic.css" />'
css_3 = '<link rel="stylesheet" type="text/css" href="https://docs.python.org/3/_static/pydoctheme.css" />'

if __name__ == "__main__":
    html_text = css_1 + css_2 + css_3
    try:
        while True:
            html_text += input("Enter the copied HTML code: \n")
    except KeyboardInterrupt:
        pass
    decoded = bs(markup=html_text, features="html.parser")
    for tag in decoded.find_all(name="a"):
        tag.target = "_blank"
    html_text = str(decoded)
    new_tag = bs(markup="<iframe />", features="html.parser")
    new_tag.iframe['width'] = "100%"
    new_tag.iframe['style'] = "border-width: 0px;"
    new_tag.iframe['scrolling'] = "no"
    new_tag.iframe['srcdoc'] = html_text
    print(new_tag)
