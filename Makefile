.PHONY: serve build

build:
	wintersmith build

serve:
	wintersmith preview

deploy:
	fab deploy

#serve:
#	cd src ; python -m SimpleHTTPServer 8000

