# Update & Upgrade Reminder

A small Python GUI that asks whether to run `sudo apt update` and `sudo apt upgrade` once a week.

## Requirements

- Debian-based Linux (Ubuntu, Debian, Kali)
- Python 3 with `tkinter`
- `schedule` (`pip install schedule`)

## Usage

    python3 UpdateUpgrade.py

Leave the script running. A window appears one week after it starts, asking "Do you want to do the update & upgrade now?" Choosing "Yes sure" runs the update in the terminal where the script was started.

## Notes

- Personal learning project from 2023.
- Run it from a terminal, since `sudo` asks for your password there.
- The window freezes while the update runs.
