PYTHON := python3
XELATEX := xelatex
DVISVGM := dvisvgm

_BUILD:
	$(PYTHON) -m mkdocs build -d build --clean

_DEPLOY:
	$(PYTHON) -m mkdocs gh-deploy -d build --message $(shell date "+%Y-%m-%d %H:%M:%S")

_CONVERT:
	$(MAKE) -f third_party/template/makefile.latex.template svg XELATEX=$(XELATEX) DVISVGM=$(DVISVGM) TEXINPUTS=$(TEXINPUTS) SILENT=1

build: | _BUILD _CONVERT
lazy-build: | _BUILD
deploy: | build _DEPLOY
lazy-deploy: | lazy-build _DEPLOY