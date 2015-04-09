.PHONY: serve build

build:
	wintersmith build

serve:
	wintersmith preview

zip:
	zip -r contents/static/pdf/all-slides.zip slides

deploy: build
	fab deploy

#serve:
#	cd src ; python -m SimpleHTTPServer 8000

