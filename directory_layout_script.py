import os
import subprocess
from pathlib import Path


def generate_directory_layout(root_dir=".", current_path=None, indent_level=0, layout=None):
    """
    Generate a directory layout with links to files for the specified root directory recursively.
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
        return "\n".join(layout)  # Handle permission errors gracefully

    # Sort directories and files alphabetically
    dirnames.sort()
    filenames.sort()

    # Compute relative path and indentation
    relative_path = os.path.relpath(current_path, root_dir)

    # Add directory name (current directory)
    if relative_path == ".":
        layout.append("📂 .")
    else:
        layout.append(f"{'│   ' * (indent_level-1)
                         }├── 📁 {os.path.basename(current_path)}")

    # Recursively call for each subdirectory (deepest first)
    for dir in dirnames:
        generate_directory_layout(root_dir, os.path.join(
            current_path, dir), indent_level + 1, layout)

    # Add files at the current level (after visiting subdirectories)
    for idx, filename in enumerate(filenames):
        repo_url = "https://github.com/abdulaziz7225/leetcode-problems/blob/main/"
        file_path = Path(current_path) / filename
        file_link = f'<a href="{repo_url}{file_path.relative_to(root_dir).as_posix()}">{
            filename}</a>'

        if idx == len(filenames) - 1:
            layout.append(f"{'│   ' * indent_level}└── {file_link}")
        else:
            layout.append(f"{'│   ' * indent_level}├── {file_link}")

    return "\n".join(layout)


def update_readme(readme_path="README.md", layout_section="### Directory Layout\n\n"):
    """
    Update the README.md file with the generated directory layout with links to files.
    """
    layout = generate_directory_layout()
    new_content = layout_section + "<pre><code>\n" + layout + "\n</code></pre>"

    # Check if the README file exists
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            readme_content = f.read()

        # Check if the layout section already exists and replace it
        if layout_section in readme_content:
            # Find the starting index of the layout section
            block_index = readme_content.index(layout_section)

            starting_block = readme_content.find("<pre><code>", block_index)
            ending_block = readme_content.find("</code></pre>", block_index)

            updated_content = readme_content[:starting_block] + "<pre><code>\n" + \
                layout + "\n</code></pre>" + readme_content[ending_block + 13:]
        else:
            updated_content = readme_content + new_content
    else:
        updated_content = new_content

    # Write the updated content to the README.md file using utf-8 encoding
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print("README.md updated successfully.")


if __name__ == "__main__":
    update_readme()
