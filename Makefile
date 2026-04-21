PYTHON ?= python3

.PHONY: check docs serve

check:
	$(PYTHON) check_links.py

docs:
	mkdocs build --clean

serve:
	mkdocs serve
