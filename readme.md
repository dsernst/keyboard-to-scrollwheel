# Keyboard-to-Scroll Mapper for macOS

This script remaps the `[` key to **scroll up** and `]` key to **scroll down** using macOS native APIs.

## Features

- Global key listener
- Native-feeling scroll in any app (e.g., Chrome, VSCode)
- Minimal dependencies

## Requirements

- macOS
- Python 3.x

## Setup (Using venv)

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Usage

Run the script:

```bash
python scroll_keys.py
```

Then press `[` or `]` to trigger vertical scrolling.

### macOS Permissions

You must grant Accessibility and Input Monitoring permissions:

1. Open System Settings → Privacy & Security → Accessibility
2. Add your terminal app (or the Python interpreter)
3. Repeat for Input Monitoring
4. Restart the script if needed

### Notes

- Scroll per keypress set as `scroll_lines` in script
- Only works while the script is running
- All scrolls are sent to the currently focused window/app

Pull requests welcome.
