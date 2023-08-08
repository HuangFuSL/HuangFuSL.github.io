---
hide:
  - navigation
---

# Welcome to HuangFuSL's blog

## :material-table-of-contents: Table of contents

* [推送](wechat/2020.md)
* [LaTeX](latex/index.md)
* [数学](math/index.md)
* [写代码](coding/index.md)
* [论文笔记](papers/index.md)
* [关于我](about.md)

## :material-timeline-clock: Blog timeline

::timeline:: class="home-timeline"

{{ build_timeline(10) }}

::/timeline::

## :material-pen-plus: Recent updates

{{ build_recent(5) }}

## :material-palette: Customization

Click on the buttons to change the primary color.

<div id="color-button">
<button data-md-color-primary="red">Red</button>
<button data-md-color-primary="pink">Pink</button>
<button data-md-color-primary="purple">Purple</button>
<button data-md-color-primary="deep-purple">Deep Purple</button>
<button data-md-color-primary="indigo">Indigo</button>
<button data-md-color-primary="blue">Blue</button>
<button data-md-color-primary="light-blue">Light Blue</button>
<button data-md-color-primary="cyan">Cyan</button>
<button data-md-color-primary="teal">Teal</button>
<button data-md-color-primary="green">Green</button>
<button data-md-color-primary="light-green">Light Green</button>
<button data-md-color-primary="lime">Lime</button>
<button data-md-color-primary="yellow">Yellow</button>
<button data-md-color-primary="amber">Amber</button>
<button data-md-color-primary="orange">Orange</button>
<button data-md-color-primary="deep-orange">Deep Orange</button>
<button data-md-color-primary="brown">Brown</button>
<button data-md-color-primary="grey">Grey</button>
<button data-md-color-primary="blue-grey">Blue Grey</button>
<button data-md-color-primary="white">White</button>
</div>

<script>
  var buttons = document.querySelectorAll("button[data-md-color-primary]");
  Array.prototype.forEach.call(buttons, function(button) {
    button.addEventListener("click", function() {
      document.body.dataset.mdColorPrimary = this.dataset.mdColorPrimary;
      localStorage.setItem("data-md-color-primary",this.dataset.mdColorPrimary);
    })
  })
</script>

Click on the buttons to change the accent color.

<div id="color-button">
<button data-md-color-accent="red">Red</button>
<button data-md-color-accent="pink">Pink</button>
<button data-md-color-accent="purple">Purple</button>
<button data-md-color-accent="deep-purple">Deep Purple</button>
<button data-md-color-accent="indigo">Indigo</button>
<button data-md-color-accent="blue">Blue</button>
<button data-md-color-accent="light-blue">Light Blue</button>
<button data-md-color-accent="cyan">Cyan</button>
<button data-md-color-accent="teal">Teal</button>
<button data-md-color-accent="green">Green</button>
<button data-md-color-accent="light-green">Light Green</button>
<button data-md-color-accent="lime">Lime</button>
<button data-md-color-accent="yellow">Yellow</button>
<button data-md-color-accent="amber">Amber</button>
<button data-md-color-accent="orange">Orange</button>
<button data-md-color-accent="deep-orange">Deep Orange</button>
</div>

<script>
  var buttons = document.querySelectorAll("button[data-md-color-accent]");
  Array.prototype.forEach.call(buttons, function(button) {
    button.addEventListener("click", function() {
      document.body.dataset.mdColorAccent = this.dataset.mdColorAccent;
      var icons = document.querySelectorAll(".gt-container .gt-avatar img[data-md-color-accent]");
      for (icon of icons)
        icon.dataset["mdColorAccent"] = this.dataset.mdColorAccent;
      localStorage.setItem("data-md-color-accent",this.dataset.mdColorAccent);
    })
  })
  document.getElementsByClassName('md-nav__title')[1].click()
</script>

However, if you try to switch from dark mode to light mode or reversed, changes
to the primary color and accent color will lose.

## :material-tools: Building documentation

Run `git clone https://github.com/HuangFuSL/HuangFuSL.github.io.git` to get the
source code.

### :bootstrap-bootstrap-fill: Bootstrap icon installation

The site uses bootstrap icons, which are neither shipped with `mkdocs-material`
nor synced in this repo. You have to manually install these icons.

* Execute the `ci/bootstrap.py` in the root directory of the repository.

### :fontawesome-brands-github: GitHub workflow

You need to install the dependencies stored in `requirements.txt` before you can
 start building the site:

```bash
pip install -r requirements.txt
```

There are cross-links in the site which require metadata defined in the page,
so the project should be built before `mkdocs serve` is executed. The exported
metadata is saved in `meta.json` after a build is successfully executed. To
build the site, execute the following command:

```bash
mkdocs build -d build
```

Execute `mkdocs serve`, the built site will appear at [http://127.0.0.1:8000](http://127.0.0.1:8000)

### :material-pen: LaTeX support

The site uses `xelatex` and `dvisvgm` to render tex document to SVG images
embedded in the markdown files. However, as the SVG images are ignored by
`.gitignore`, you have to manually perform the conversion.

For GitHub repository clones:

* Run `git submodule update --recursive --remote` to receive the template.
* Make sure you have installed and correctly configured `xelatex` and `dvisvgm`.
* Add `./template` directory to `$TEXINPUTS` environmental variable.
* Execute `ci/convert.py` in the root directory of the repository.
* Run `mkdocs serve` to view the images.

The template is located at [HuangFuSL/latex-template](https://github.com/HuangFuSL/latex-template)

## :material-lightbulb-on: Acknowledgements

The blog relies on the following open-source projects:

* [mkdocs](https://github.com/mkdocs/mkdocs)
* [Python Markdown](https://github.com/Python-Markdown/markdown)
* [Python Markdown Extension](https://github.com/facelessuser/pymdown-extensions)
* [matplotlib](https://github.com/matplotlib/matplotlib)
* [pandas](https://github.com/pandas-dev/pandas)
* [jupyter](https://github.com/jupyter/jupyter)
* [requests](https://github.com/psf/requests)
* [lxml](https://github.com/lxml/lxml)

The blog uses the following mkdocs plugins to function correctly.

* [Neoteroi/mkdocs-plugins](https://github.com/Neoteroi/mkdocs-plugins)
* [lukasgeiter/mkdocs-awesome-pages-plugin](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin)
* [timvink/mkdocs-git-revision-date-localized-plugin](https://github.com/timvink/mkdocs-git-revision-date-localized-plugin)
* [zhaoterryy/mkdocs-git-revision-date-plugin](https://github.com/zhaoterryy/mkdocs-git-revision-date-plugin)
* [squidfunk/mkdocs-material](https://github.com/squidfunk/mkdocs-material)
* [facelessuser/mkdocs-material-extensions](https://github.com/facelessuser/mkdocs-material-extensions)
* [fralau/mkdocs_macros_plugin](https://github.com/fralau/mkdocs_macros_plugin)
* [danielfrg/mkdocs-jupyter](https://github.com/danielfrg/mkdocs-jupyter)
* [prcr/mkdocs-meta-descriptions-plugin](https://github.com/prcr/mkdocs-meta-descriptions-plugin)

Unless noted, content in this blog are shared under [CC-BY-NC-SA 4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/) license.

## :material-update: Version information

<div style="white-space: pre-line;">{{ git.raw }}</div>