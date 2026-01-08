import csv

def save_posts(posts: list, output_path: str):
    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["day", "post_type", "content"]
        )
        writer.writeheader()
        writer.writerows(posts)
