#!bin/sh
cp scrum-archive/* docs/scrums/
python update_scrum.py
mkdocs build -d ../docs
