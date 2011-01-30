build: optimizePNG
	cp ./src/*.vcf ./build/
	python ./scripts/builder.py
	scp ./build/* prgmr:/home/mikewest/public_html/mkw.st/public/

optimizePNG: ./src/*.png
	@optipng -o7 ./src/*.png
