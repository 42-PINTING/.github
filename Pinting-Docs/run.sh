#!bin/sh
cp scrum-archive/* docs/scrums/
mkdocs build -d ../docs
# python attach_newfile.py
