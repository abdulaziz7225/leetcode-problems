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
        questionId
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
        problem_number = f"{question_data['questionId']}. {question_data['title']}"
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

        file_name = f"{question_data['questionId']}.{title_slug.replace('-', '_')}.py"
        file_path = os.path.join(full_path, file_name)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(comment)

        print(f"Success! File saved to: {file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    url_input = input("Enter a link to LeetCode problem: ")
    dir_input = input("Enter a directory name: ")
    get_problem_data(url_input, dir_input if dir_input else ".")
