build: optimizePNG
	cp ./src/*.vcf ./build/
	python ./scripts/builder.py

optimizePNG: ./src/*.png
	@optipng -o7 ./src/*.png
