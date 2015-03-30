.PHONY: serve build

build:
	wintersmith build

serve:
	wintersmith preview

deploy: build
	fab deploy

#serve:
#	cd src ; python -m SimpleHTTPServer 8000

