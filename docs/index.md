---
hide:
  - navigation
  - toc
template: _toc.html
---

# Welcome to HuangFuSL's blog

## :material-table-of-contents: Table of contents

* [推送](wechat/2020.md)
* [都市天际线](csl/index.md)
* [LaTeX](latex/index.md)
* [数学](math/index.md)
* [写代码](coding/index.md)
* [关于我](about.md)

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

Run `git clone https://github.com/HuangFuSL/HuangFuSL.github.io.git` or
`docker push huangfusl/huangfusl.github.io:latest` to get the code.

> Docker image is built at 8:00 AM (UTC) every two days, starting from the first
>  day of each month

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

### LaTeX support

The site uses `xelatex` and `dvisvgm` to render tex document to SVG images
embedded in the markdown files. However, as the SVG images are ignored by
`.gitignore`, you have to manually perform the conversion.

For GitHub repository clones:

* Make sure you have installed and correctly configured `xelatex` and `dvisvgm`.
* Execute the `ci/convert.py` in the root directory of the repository.
* Run `mkdocs serve` to view the images.

## :material-update: Version information

<div style="white-space: pre-line;">{{ git.raw }}</div>