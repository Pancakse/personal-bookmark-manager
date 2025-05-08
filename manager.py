import json
import os

BOOKMARK_FILE = 'bookmarks/bookmarks.json'

def load_bookmarks():
    if not os.path.exists(BOOKMARK_FILE):
        return []
    
    with open(BOOKMARK_FILE, 'r') as file:
        return json.load(file)

def save_bookmarks(bookmarks):
    with open(BOOKMARK_FILE, 'w') as file:
        json.dump(bookmarks, file, indent=4)

def add_bookmark(url, description):
    bookmarks = load_bookmarks()
    bookmarks.append({"url": url, "description": description})
    save_bookmarks(bookmarks)
    print(f"Bookmark added: {url}")

def view_bookmarks():
    bookmarks = load_bookmarks()
    if not bookmarks:
        print("No bookmarks saved.")
        return
    
    for i, bookmark in enumerate(bookmarks, 1):
        print(f"{i}. {bookmark['description']}: {bookmark['url']}")

def delete_bookmark(index):
    bookmarks = load_bookmarks()
    if index < 1 or index > len(bookmarks):
        print("Invalid index.")
        return
    
    deleted = bookmarks.pop(index - 1)
    save_bookmarks(bookmarks)
    print(f"Deleted bookmark: {deleted['description']}: {deleted['url']}")
