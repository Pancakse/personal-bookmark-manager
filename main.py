import sys
from manager import add_bookmark, view_bookmarks, delete_bookmark

def print_help():
    print("Personal Bookmark Manager")
    print("Usage:")
    print("  python main.py add <URL> <description>    - Add a bookmark")
    print("  python main.py view                       - View all bookmarks")
    print("  python main.py delete <index>             - Delete a bookmark")

def main():
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1]
    
    if command == "add" and len(sys.argv) == 4:
        add_bookmark(sys.argv[2], sys.argv[3])
    elif command == "view":
        view_bookmarks()
    elif command == "delete" and len(sys.argv) == 3:
        try:
            index = int(sys.argv[2])
            delete_bookmark(index)
        except ValueError:
            print("Invalid index.")
    else:
        print_help()

if __name__ == "__main__":
    main()
