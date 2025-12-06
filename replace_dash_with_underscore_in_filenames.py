import os

def rename_files_interactive(root_dir):
    """
    Scans for files with dashes, shows a preview, and asks for confirmation
    before renaming.
    """
    changes_map = []
    
    # 1. SCAN AND COLLECT CHANGES
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip hidden directories like .git
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]

        for filename in filenames:
            if '-' in filename:
                new_filename = filename.replace('-', '_')
                old_path = os.path.join(dirpath, filename)
                new_path = os.path.join(dirpath, new_filename)
                
                # Store the change to process later
                changes_map.append((old_path, new_path, filename, new_filename))

    # 2. IF NO CHANGES, EXIT
    if not changes_map:
        print("No files with dashes found. Exiting.")
        return

    # 3. SHOW PREVIEW
    print(f"Found {len(changes_map)} files to rename:\n")
    for old, new, fname, new_fname in changes_map:
        print(f"[PREVIEW] {fname}  -->  {new_fname}")
    
    # 4. ASK FOR PERMISSION
    print("-" * 40)
    user_input = input("Do you want to apply these changes now? (y/n): ").lower().strip()

    if user_input != 'y':
        print("Aborted. No changes were made.")
        return

    # 5. APPLY CHANGES
    print("\nApplying changes...")
    count = 0
    for old_path, new_path, fname, new_fname in changes_map:
        if os.path.exists(new_path):
            print(f"[SKIP] Target exists: {new_fname}")
            continue
            
        try:
            os.rename(old_path, new_path)
            # print(f"[DONE] {new_fname}") # Optional: Uncomment for noisy output
            count += 1
        except OSError as e:
            print(f"[ERROR] Failed to rename {fname}: {e}")

    print(f"\nSuccess! Renamed {count} files.")

if __name__ == "__main__":
    current_directory = os.getcwd()
    rename_files_interactive(current_directory)