PORT=8000
OUTPUT_DIR=./docs

build:
	./build.sh

clean:
	rm -rf ./dist/*

run:
	python -m http.server $(PORT) --directory $(OUTPUT_DIR)