# syntax=docker/dockerfile:1

FROM python:3.12.3-alpine3.19

RUN pip install --upgrade pip && \
	pip install mkdocs

CMD ["mkdocs", "serve", "-a", "0.0.0.0:8888"]
