import os
import re
import requests
import time
import sys

# --- CONFIGURATION ---
ROOT_DIR = "."
API_URL = "https://leetcode.com/graphql"
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}

# Directories to strictly ignore during traversal
IGNORED_DIRS = {
    "__pycache__",
    ".git",
    ".vscode",
    ".idea",
    ".env",           # Just in case it's a folder
    "venv",
    ".venv",
    "env",
    "ENV",
    ".pytest_cache",
    ".mypy_cache",
    ".tox",
    ".nox",
    "build",
    "dist",
    "htmlcov",
    ".ipynb_checkpoints",
    "site-packages",
    "node_modules",
    "__pypackages__",
    "cython_debug"
}


class PendingChange:
    def __init__(self, original_path, new_path, new_content, change_type):
        self.original_path = original_path
        self.new_path = new_path
        self.new_content = new_content
        self.change_type = change_type  # 'RENAME', 'UPDATE', 'BOTH'


def get_correct_details(url):
    try:
        slug = url.split("/problems/")[1].split("/")[0]
    except IndexError:
        return None

    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionFrontendId
        title
      }
    }
    """
    try:
        response = requests.post(API_URL, json={"query": query, "variables": {
                                 "titleSlug": slug}}, headers=HEADERS)
        if response.status_code != 200:
            return None
        data = response.json().get("data", {}).get("question")
        if not data:
            return None
        return {
            "id": data["questionFrontendId"],
            "title": data["title"],
            "slug": slug
        }
    except:
        return None


def analyze_file(file_path, filename):
    """
    Reads a file, queries API, and determines if changes are needed.
    Returns a PendingChange object or None.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception:
        return None

    # 1. Extract Link
    link = None
    for line in lines[:10]:
        if "Link: https://leetcode.com/problems/" in line:
            match = re.search(
                r"Link: (https://leetcode\.com/problems/[\w-]+)", line)
            if match:
                link = match.group(1)
                break

    if not link:
        return None

    # 2. API Call (This is slow but necessary for the preview)
    data = get_correct_details(link)
    if not data:
        print(f"[WARN] API failed for file: {filename}")
        return None

    correct_id = data["id"]
    correct_title = data["title"]
    correct_slug = data["slug"]

    # 3. Check Content
    new_lines = lines[:]
    content_changed = False
    expected_line = f"Problem Number: {correct_id}. {correct_title}\n"

    for i, line in enumerate(new_lines[:10]):
        if "Problem Number:" in line:
            if line != expected_line:
                new_lines[i] = expected_line
                content_changed = True
            break

    # 4. Check Filename
    new_filename = f"{correct_id}.{correct_slug.replace('-', '_')}.py"
    rename_needed = filename != new_filename

    if not content_changed and not rename_needed:
        return None

    # Determine Change Type
    if content_changed and rename_needed:
        c_type = "BOTH"
    elif rename_needed:
        c_type = "RENAME"
    else:
        c_type = "UPDATE"

    full_new_path = os.path.join(os.path.dirname(file_path), new_filename)

    return PendingChange(file_path, full_new_path, new_lines, c_type)


def main():
    print("--- SCANNING FILES & FETCHING DATA ---")
    print(f"Ignoring directories: {', '.join(sorted(list(IGNORED_DIRS)))}")
    print("Fetching correct IDs from LeetCode... this may take a moment due to rate limits.")

    changes = []
    scanned_count = 0

    # topdown=True is required to modify 'dirs' in-place
    for root, dirs, files in os.walk(ROOT_DIR, topdown=True):

        # ---------------------------------------------------------
        # EXCLUSION LOGIC: Remove ignored dirs from traversal list
        # ---------------------------------------------------------
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]

        for file in files:
            if file.endswith(".py") and file != os.path.basename(__file__):
                full_path = os.path.join(root, file)

                # Progress indicator
                print(f"\rScanning: {file[:40].ljust(40)}", end="", flush=True)

                change = analyze_file(full_path, file)
                if change:
                    changes.append(change)

                # Rate limit protection (approx 200ms delay)
                time.sleep(0.2)
                scanned_count += 1

    print(f"\n\n--- PROPOSED CHANGES ({len(changes)}) ---")

    if not changes:
        print("No changes needed. All files are correct.")
        return

    # Print Report
    for c in changes:
        old_name = os.path.basename(c.original_path)
        new_name = os.path.basename(c.new_path)

        if c.change_type == "RENAME":
            print(f"[RENAME] {old_name}  -->  {new_name}")
        elif c.change_type == "UPDATE":
            print(f"[CONTENT] {old_name}  (Updating 'Problem Number' line)")
        elif c.change_type == "BOTH":
            print(f"[BOTH]   {old_name}  -->  {new_name} (+ Content Update)")

    # Confirmation
    print("-" * 60)
    confirm = input(
        "Do you want to apply these changes? (y/n): ").strip().lower()

    if confirm != 'y':
        print("Aborted. No changes made.")
        sys.exit(0)

    # Execution Phase
    print("\n--- APPLYING CHANGES ---")
    for c in changes:
        try:
            # 1. Update Content first
            with open(c.original_path, "w", encoding="utf-8") as f:
                f.writelines(c.new_content)

            # 2. Rename if needed
            if c.change_type in ["RENAME", "BOTH"]:
                # Check for collision
                if os.path.exists(c.new_path):
                    print(
                        f"Skipping rename for {os.path.basename(c.original_path)}: Target exists.")
                else:
                    os.rename(c.original_path, c.new_path)
                    print(f"Processed: {os.path.basename(c.new_path)}")
            else:
                print(f"Processed: {os.path.basename(c.original_path)}")

        except Exception as e:
            print(f"Error processing {c.original_path}: {e}")

    print("Done.")


if __name__ == "__main__":
    main()
