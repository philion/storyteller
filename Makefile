.PHONY: all run clean

VENV = .env
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

run: $(VENV)/bin/activate
	$(PYTHON) zmachine games/hhgg.z3

$(VENV)/bin/activate: requirements.txt
	
env:
	python3 -m venv $(VENV)
	echo "run: source ./$(VENV)/bin/activate"
	
requirements:
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

all: $(VENV)/bin/activate

clean:
	rm -rf __pycache__
	rm -rf $(VENV)
	find . -type f -name ‘*.pyc’ -delete