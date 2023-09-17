_BUILD:
	python3 -m mkdocs build -d build --clean

_DEPLOY:
	python3 -m mkdocs gh-deploy -d build --message $(shell date "+%Y-%m-%d %H:%M:%S")

_CONVERT:
	make -f third_party/template/makefile.latex.template svg

convert: _CONVERT
build: _BUILD
deploy: | build _DEPLOY
