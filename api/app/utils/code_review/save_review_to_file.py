import os
from datetime import datetime

REVIEW_FOLDER = "reviews"

def save_review_to_file(html_string: str) -> str:
    os.makedirs(REVIEW_FOLDER, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"CodeReview_{timestamp}.html"
    file_path = os.path.join(REVIEW_FOLDER, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_string)

    return file_path, filename