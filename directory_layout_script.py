import os
import subprocess


def generate_directory_layout(root_dir=".", current_path=None, indent_level=0, layout=None):
    """
    Generate a directory layout for the specified root directory recursively.
    This function starts appending files from the deepest directory upwards.
    """

    if layout is None:
        layout = []

    if current_path is None:
        current_path = root_dir

    # List directories and files, excluding hidden ones
    try:
        dirnames, filenames = [], []
        with os.scandir(current_path) as entries:
            for entry in entries:
                if entry.is_dir() and not entry.name.startswith('.'):
                    dirnames.append(entry.name)
                elif entry.is_file() and not entry.name.startswith('.'):
                    filenames.append(entry.name)
    except PermissionError:
        return "\n".join(layout) # Handle permission errors gracefully
    
    # Sort directories and files alphabetically
    dirnames.sort()
    filenames.sort()

    # Compute relative path and indentation
    relative_path = os.path.relpath(current_path, root_dir)
    
    # Add directory name (current directory)
    if relative_path == ".":
        layout.append(".")
    else:
        layout.append(f"{'│   ' * (indent_level-1)}├── {os.path.basename(current_path)}")

    # Recursively call for each subdirectory (deepest first)
    for dir in dirnames:
        generate_directory_layout(root_dir, os.path.join(current_path, dir), indent_level + 1, layout)

    # Add files at the current level (after visiting subdirectories)
    for idx, filename in enumerate(filenames):
        if idx == len(filenames) - 1:
            layout.append(f"{'│   ' * indent_level}└── {filename}")
        else:
            layout.append(f"{'│   ' * indent_level}├── {filename}")

    return "\n".join(layout)
    
def update_readme(readme_path="README.md", layout_section="### Directory Layout\n\n"):
    """
    Update the README.md file with the generated directory layout.
    """
    
    layout = generate_directory_layout()
    new_content = layout_section + "```\n" + layout + "\n```"
    
    # Check if the README file exists
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            readme_content = f.read()
            
        # Check if the layout section already exists and replace it
        if layout_section in readme_content:
            # Find the starting index of the layout section
            start_index = readme_content.index(layout_section)
            
            first_backtick = readme_content.find("```", start_index + len(layout_section))
            second_backtick = readme_content.find("```", first_backtick + 3)
            
            updated_content = readme_content[:first_backtick] + "```README\n" + layout + "\n```" + readme_content[second_backtick + 3:]
        else:
            updated_content = readme_content + new_content
    else:
        updated_content = new_content

    # Write the updated content to the README.md file using utf-8 encoding
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated_content)
        
    print("README.md updated successfully.")

def get_added_and_deleted_files():
    """
    Get the list of newly added files (status 'A' from git).
    """
    try:
        # Run git status in porcelain mode to get the status of files
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        result.check_returncode()

        # Filter out the added ('A') and deleted ('D') files
        added_files = [line[3:] for line in result.stdout.splitlines() if line.startswith("A ")]
        deleted_files = [line[3:] for line in result.stdout.splitlines() if line.startswith("D ")]
        
        return added_files, deleted_files
    except subprocess.CalledProcessError as e:
        print(f"Error checking git status: {e}")
        return []
    
def main():
    # Get newly added and deleted files in the repository
    added_files, deleted_files = get_added_and_deleted_files()
    
    if added_files or deleted_files:
        print("New or deleted files detected:")
        print("Added:", added_files)
        print("Deleted:", deleted_files)
        update_readme()  # Update README if new files are added
    else:
        print("No new or deleted files to update README.")
        
if __name__ == "__main__":
    # main()
    update_readme()