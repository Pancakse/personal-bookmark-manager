# Personal Bookmark Manager

A simple CLI-based bookmark manager to save, view, and delete your bookmarks.

## Features
- Add bookmarks with a URL and description.
- View all saved bookmarks.
- Delete bookmarks by index.

## Sample Usage
1. Clone this repo:
   ```bash
   git clone https://github.com/Pancakse/personal-bookmark-manager.git
   cd personal-bookmark-manager

2. Run the bookmark manager:
   python main.py add "https://github.com" "GitHub"
   python main.py view
   python main.py delete 1

## Bookmarks Storage

Bookmarks are stored in a local JSON file: bookmarks/bookmarks.json.

## Requirements

    Python 3.6+

    No external libraries required (standard Python only)
