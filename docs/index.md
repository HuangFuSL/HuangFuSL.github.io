---
hide:
  - navigation
  - toc
template: _toc.html
---

# Welcome to HuangFuSL's blog

[![Build Docker Image](https://github.com/HuangFuSL/HuangFuSL.github.io/actions/workflows/docker.yml/badge.svg)](https://github.com/HuangFuSL/HuangFuSL.github.io/actions/workflows/docker.yml) ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/HuangFuSL/HuangFuSL.github.io?color=brightgreen&logo=github&logoColor=lightgrey) ![Docker Pulls](https://img.shields.io/docker/pulls/huangfusl/huangfusl.github.io?color=brightgreen&logo=docker) ![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/huangfusl/huangfusl.github.io?logo=docker) [![URL](https://img.shields.io/badge/URL-huangfusl.github.io-brightgreen)](https://huangfusl.github.io/index.html)

## :material-table-of-contents: Table of contents

* [推送](wechat/2020.md)
* [LaTeX](latex/index.md)
* [数学](math/index.md)
* [写代码](coding/index.md)
* [COVID-19](covid.md)
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

For GitHub repository clones:

* Execute the `ci/bootstrap.py` in the root directory of the repository.

For Docker containers:

* No addition setup required.

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

### :fontawesome-brands-docker: Docker workflow

Start a container using the pulled image, remember to properly set the port
to be published.

```bash
docker run -p 8000:8000 huangfusl/huangfusl.github.io
```

If you want to edit the content of the blog, remember your changes will LOSE if
the image is deleted as the data is not stored in a data volume. You should
switch to the forked branch and perform a commit on that branch.

### LaTeX support

The site uses `xelatex` and `dvisvgm` to render tex document to SVG images
embedded in the markdown files. However, as the SVG images are ignored by
`.gitignore`, you have to manually perform the conversion.

For GitHub repository clones:

* Make sure you have installed and correctly configured `xelatex` and `dvisvgm`.
* Execute the `ci/convert.py` in the root directory of the repository.
* Run `mkdocs serve` to view the images.

For Docker containers:

* To reduce docker image size, texlive environment is not installed. You should
  install texlive manually.
* Open the terminal and execute `ci/convert.py`.
* Wait for `mkdocs` building the site.
* View the site at [http://127.0.0.1:8000](http://127.0.0.1:8000)

### :material-comment-text: Comment system

The site uses [Gitalk](https://github.com/gitalk/gitalk/) for commenting
functionality. However as the backend GitHub OAuth application is registered for
only `huangfusl.github.io`, you *CANNOT* use the comment system unless you push
to this repository.

To enable comment feature on your own site, please follow the following
instructions:

1. Create a GitHub OAuth application at
  [here](https://github.com/settings/applications/new). Set both "Homepage URL"
  and "Authorization callback URL" to the URL of your own site. After the
  application is created, copy the client ID and the client secret.  
2. Create two repository secrets named `GITALK_ID` and `GITALK_SECRET`. Paste
  the value you've copied.  
3. Create a repository to hold the issues (or use an existing one), modify the
  following part in `overrides/_main.html`
  ```html
  <script type="text/javascript">
      const gitalk = new Gitalk({
          clientID: '%s',
          clientSecret: '%s',
          repo: 'Comments',      // The repository of store comments,
          owner: 'HuangFuSL',
          admin: ['HuangFuSL'],
          id: hex_md5(location.pathname), // Ensure uniqueness and length less than 50
          distractionFreeMode: false  // Facebook-like distraction free mode
      })
      gitalk.render('gitalk-container')
  </script>
  ```
  Change the value of `repo` to the name of your own repository, `owner` to the
  owner of the repository. If you want someone to manage the comments, add their
  name to the `admin` field. For more config options, please refer to
  [Gitalk repository](https://github.com/gitalk/gitalk).  
4. Push the repository to GitHub.  
5. After GitHub actions has finished, view the deployed site.  

## Coding Records

<center><embed src="https://wakatime.com/share/@9eb40973-374b-44b8-8353-8ba5c8510373/e274b6f5-30c6-41a3-ba23-549ff34364c0.svg" width="50%"></center>

## :material-update: Version information

<div style="white-space: pre-line;">{{ git.raw }}</div>