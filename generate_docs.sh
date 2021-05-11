#!/usr/bin/env bash

FILENAME="src/app/__init__.py"

printf "import django\n\ndjango.setup()" > $FILENAME

export DJANGO_SETTINGS_MODULE=app.settings

pdoc --pdf --force --output-dir docs/ src/app/ > docs/result.md 
pandoc --metadata=title:"Python_Django_Test" --variable=mainfont:"DejaVu Sans" --toc --toc-depth=4 -s docs/result.md -o docs/index.html

echo "" > $FILENAME