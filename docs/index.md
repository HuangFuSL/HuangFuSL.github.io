# Welcome to HuangFuSL's blog

[![Build Docker Image](https://github.com/HuangFuSL/HuangFuSL.github.io/actions/workflows/docker.yml/badge.svg)](https://github.com/HuangFuSL/HuangFuSL.github.io/actions/workflows/docker.yml) ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/HuangFuSL/HuangFuSL.github.io?color=brightgreen&logo=github&logoColor=lightgrey) ![Docker Pulls](https://img.shields.io/docker/pulls/huangfusl/huangfusl.github.io?color=brightgreen&logo=docker) ![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/huangfusl/huangfusl.github.io?logo=docker) [![URL](https://img.shields.io/badge/URL-huangfusl.github.io-brightgreen)](https://huangfusl.github.io/index.html)

## Customization

点击下面的颜色按钮可以切换主题颜色：

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

点击下面的按钮可以切换强调颜色：

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

## Building documentation

Run `git clone https://github.com/HuangFuSL/HuangFuSL.github.io.git` or
`docker push huangfusl/huangfusl.github.io:latest` to get the code.

### GitHub workflow

After cloning the repository, install the dependencies stored in `requirements.txt`:

```bash
pip install -r requirements.txt
```

Execute `mkdocs serve`, the built site will appear at [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Docker workflow

Start a container using the pulled image, remember to properly set the port
publishing.

```bash
docker run -p 8000:8000 huangfusl/huangfusl.github.io
```

If you want to edit the content of the blog, remember your changes will LOSE if
the image is deleted as the data is not stored in a data volume. You should
switch to the forked branch and perform a commit on that branch.