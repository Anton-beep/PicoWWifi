***To use install Thonny IDE.***

`main.py` runs `src/main.py`, this is made to easilly upload src directory (and all files inside it) to the board using Thonny.

# Run
Open Thonny, connect to pico w, copy src and main.py to the board

# Tests
To run tests run `src/tests/test_test.py` from Thonny 

# Typing and formatting
This section is about tools, which are helping during development.

Create and activate .venv:
**Change activate command on Windows**
```
python -m venv .venv
source .venv/bin/activate
```

```
python install -r requirements.txt
```

Install stubs for typing using `pip install -U  micropython-rp2-pico_w-stubs --target typings --no-user` and configure using https://micropython-stubs.readthedocs.io/en/main/22_vscode.html

run black: 

black src