.PHONY: install run clean

VENV := .venv
PY := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

$(PY):
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip

install: $(PY)
	$(PIP) install -r requirements.txt

run: install
	$(PY) diffuse_logic.py

clean:
	rm -rf $(VENV)
