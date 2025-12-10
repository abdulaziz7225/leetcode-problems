import requests
import os
from bs4 import BeautifulSoup


def get_problem_data(url: str, directory_path: str = "."):
    # 1. Extract the "slug" from the URL
    try:
        # Handles urls like https://leetcode.com/problems/number-complement/description/
        title_slug = url.split("/problems/")[1].split("/")[0]
    except IndexError:
        return "Error: Invalid LeetCode URL."

    # 2. Define the GraphQL Query
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionFrontendId
        title
        difficulty
        content
      }
    }
    """

    # 3. Set up headers and payload
    api_url = "https://leetcode.com/graphql"
    payload = {
        "query": query,
        "variables": {"titleSlug": title_slug}
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Referer": url
    }

    try:
        # 4. Fetch Data
        print(f"Fetching data for: {title_slug}...")
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()

        data = response.json()
        question_data = data["data"]["question"]

        if not question_data:
            print("Error: Problem not found.")
            return

        # 5. Extract and Format Data
        problem_number = f"{question_data['questionFrontendId']}. {question_data['title']}"
        difficulty = question_data['difficulty']

        # --- HTML CLEANING LOGIC ---
        raw_html = question_data['content']
        soup = BeautifulSoup(raw_html, "html.parser")
        clean_text = soup.get_text()

        # Post-processing to make it look neat (remove excessive empty lines)
        lines = [line.strip() for line in clean_text.splitlines()]
        # Remove empty strings from list while preserving paragraph breaks
        cleaned_content = "\n".join([line for line in lines if line])

        # Fix specific headers to have a newline before them for readability
        cleaned_content = cleaned_content.replace("Example", "\nExample")
        cleaned_content = cleaned_content.replace(
            "Constraints:", "\nConstraints:")
        cleaned_content = cleaned_content.replace("Follow up:", "\nFollow up:")
        # ---------------------------

        # 6. Construct the final string
        # Removing '/description' from url for the clean link
        clean_link = url.split("/description")[0]

        comment = f"""\"\"\"\nProblem Number: {problem_number}\nDifficulty Level: {difficulty}\nLink: {clean_link}\n\n********************************************************************************\n\n{cleaned_content}\n\"\"\""""

        # 7. Write to file
        full_path = os.path.join(directory_path, difficulty.lower())
        os.makedirs(full_path, exist_ok=True)

        file_name = f"{question_data['questionFrontendId']}.{title_slug.replace('-', '_')}.py"
        file_path = os.path.join(full_path, file_name)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(comment)

        print(f"Success! File saved to: {file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


def resolve_directory(partial_name):
    """
    Attempts to autocomplete a directory name based on partial input.
    - If partial_name matches an existing folder exactly, returns it.
    - If partial_name matches the start of exactly one folder, returns that folder.
    - Otherwise, returns the original partial_name (letting mkdir handle creation later).
    """
    if not partial_name or partial_name == ".":
        return "."

    # Get all items in current directory
    try:
        all_items = os.listdir(".")
    except OSError:
        return partial_name

    # Filter for directories that start with the input (case-insensitive for better UX)
    candidates = [
        item for item in all_items
        if os.path.isdir(item) and item.lower().startswith(partial_name.lower())
    ]

    # LOGIC:
    # 1. Exact match preference (e.g., user typed "tree" and "tree" exists)
    if partial_name in candidates:
        return partial_name

    # 2. Autocomplete if exactly one match found (e.g., user typed "bin", found "binary-search")
    if len(candidates) == 1:
        print(
            f"--> Autocompleted directory: '{partial_name}' to '{candidates[0]}'")
        return candidates[0]

    # 3. Ambiguous (multiple matches) or no match -> Return original input
    if len(candidates) > 1:
        print(
            f"--> Ambiguous input '{partial_name}'. Found: {candidates}. Using '{partial_name}'.")

    return partial_name


if __name__ == "__main__":
    url_input = input("Enter a link to LeetCode problem: ").strip()
    dir_input_raw = input("Enter a directory name: ").strip()

    # Resolve the directory name before passing it to the main function
    final_dir = resolve_directory(dir_input_raw) if dir_input_raw else "."

    get_problem_data(url_input, final_dir)
