_BUILD:
	python3 -m mkdocs build -d build --dirty

_DEPLOY:
	python3 -m mkdocs gh-deploy -d build --message "Update on $(shell date "+%Y-%m-%d %H:%M:%S")" --dirty

_CONVERT:
	make -f third_party/template/makefile.latex.template svg

_PUSH:
	git add .
	git commit -m "Update on $(shell date "+%Y-%m-%d %H:%M:%S")"
	git push

convert: _CONVERT
build: _BUILD
deploy: | build _DEPLOY
push: | build _PUSH
