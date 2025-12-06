import os

def rename_folders_interactive(root_dir):
    print(f"Scanning directories in: {root_dir}...\n")
    
    # 1. DEFINE FOLDERS TO STRICTLY IGNORE
    # If a path contains ANY of these, we skip it entirely.
    IGNORED_ROOTS = {'.git', '.env', 'venv', '.venv', '__pycache__', '.idea', '.vscode'}

    changes_map = []

    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        
        # --- SAFETY CHECK ---
        # Split the current path into parts (e.g., "coding/dsa/.env/lib/site-packages")
        # If any part of the path is in IGNORED_ROOTS, we are inside a forbidden zone.
        path_parts = dirpath.split(os.sep)
        if any(part in IGNORED_ROOTS for part in path_parts):
            continue
        # --------------------

        for dirname in dirnames:
            # Skip hidden directories (starting with .) 
            # and explicitly ignored ones if they appear as immediate children
            if dirname.startswith('.') or dirname in IGNORED_ROOTS:
                continue

            # TRANSFORMATION RULES:
            # 1. Replace underscore with dash
            # 2. Convert to lowercase
            new_dirname = dirname.replace('_', '-').lower()

            # Only proceed if the name actually needs changing
            if new_dirname != dirname:
                old_path = os.path.join(dirpath, dirname)
                new_path = os.path.join(dirpath, new_dirname)
                
                changes_map.append((old_path, new_path, dirname, new_dirname))

    # IF NO CHANGES
    if not changes_map:
        print("No folders found that need renaming.")
        return

    # PREVIEW
    print(f"Found {len(changes_map)} folders to rename:\n")
    for old, new, dname, new_dname in changes_map:
        print(f"[PREVIEW] {dname}  -->  {new_dname}")

    # CONFIRMATION
    print("-" * 40)
    user_input = input("Do you want to apply these changes now? (y/n): ").lower().strip()

    if user_input != 'y':
        print("Aborted. No changes were made.")
        return

    # EXECUTE
    print("\nApplying changes...")
    count = 0
    for old_path, new_path, dname, new_dname in changes_map:
        if os.path.exists(new_path):
            print(f"[SKIP] Target already exists: {new_dname}")
            continue

        try:
            os.rename(old_path, new_path)
            count += 1
        except OSError as e:
            print(f"[ERROR] Could not rename {dname}: {e}")

    print(f"\nSuccess! Renamed {count} folders.")

if __name__ == "__main__":
    current_directory = os.getcwd()
    rename_folders_interactive(current_directory)