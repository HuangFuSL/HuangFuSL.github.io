PYTHON := python3
XELATEX := xelatex
DVISVGM := dvisvgm

_BUILD:
	$(PYTHON) -m mkdocs build -d build --clean

_DEPLOY:
	$(PYTHON) -m mkdocs gh-deploy -d build --message $(shell date "+%Y-%m-%d %H:%M:%S")

_CONVERT:
	$(MAKE) -j 4 -f third_party/template/makefile.latex.template svg XELATEX=$(XELATEX) DVISVGM=$(DVISVGM) TEXINPUTS=$(TEXINPUTS) SILENT=1 COMPILE_NUM=1

test-code-block:
	for i in $$(find docs -name "*.md" -and -not -name "pyguide.md"); do \
		$(PYTHON) -m doctest -o ELLIPSIS -o IGNORE_EXCEPTION_DETAIL $$i; \
	done

build: | _BUILD _CONVERT
lazy-build: | _BUILD
deploy: | build _DEPLOY
lazy-deploy: | lazy-build _DEPLOY