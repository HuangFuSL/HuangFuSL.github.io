PYTHON := python3
XELATEX := xelatex
DVISVGM := dvisvgm

_BUILD:
	$(PYTHON) -m mkdocs build -d build --clean

_DEPLOY:
	$(PYTHON) -m mkdocs gh-deploy -d build --message $(shell date "+%Y-%m-%d %H:%M:%S")

_CONVERT:
	$(MAKE) -j 4 -f third_party/template/makefile.latex.template svg XELATEX=$(XELATEX) DVISVGM=$(DVISVGM) TEXINPUTS=$(TEXINPUTS) SILENT=1 &> /dev/null

build: | _BUILD _CONVERT
lazy-build: | _BUILD
deploy: | build _DEPLOY
lazy-deploy: | lazy-build _DEPLOY