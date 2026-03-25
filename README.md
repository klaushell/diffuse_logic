# diffuseLogic

Small fuzzy-logic demo using [scikit-fuzzy](https://github.com/scikit-fuzzy/scikit-fuzzy): distance and speed map to a suggested crossing pace (walking, trotting, running). Running the script prints the defuzzified output and opens matplotlib plots for the membership functions.

## Requirements

- Python 3.10 or newer
- `make` (optional; you can run commands manually)

## Quick start

```bash
make run
```

This creates a virtual environment in `.venv`, installs dependencies, runs `diffuse_logic.py`, and shows the plots.

## Manual setup

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
python diffuse_logic.py
```

## Makefile targets

| Target    | Description                                      |
| --------- | ------------------------------------------------ |
| `install` | Create `.venv` (if needed) and install packages |
| `run`     | Install (if needed) and run `diffuse_logic.py`  |
| `clean`   | Remove `.venv`                                  |

## Project layout

- `diffuse_logic.py` — fuzzy control system and visualization
- `requirements.txt` — Python dependencies
- `Makefile` — venv, install, and run shortcuts
