import yaml
from planner import generate_plan
from prompt_engine import build_prompt
from generator import generate_post
from storage import save_posts
import random


def load_brand_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def load_prompt_template(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read()
    
HOOKS = {
    "educational": [
        "A simple breakdown most founders overlook",
        "A practical explanation without buzzwords",
        "A step-by-step approach that actually works"
    ],
    "insight": [
        "A counterintuitive observation from real workflows",
        "What most people misunderstand about this",
        "An overlooked reality in small businesses"
    ],
    "mistake": [
        "A mistake I see repeatedly",
        "A costly assumption founders make",
        "Where automation projects usually fail"
    ],
    "tip": [
        "A quick win you can implement this week",
        "A low-effort improvement with high ROI",
        "One small change that saves hours"
    ]
}



def main():
    brand = load_brand_config("config/brand.yaml")
    template = load_prompt_template("prompts/linkedin.txt")

    plan = generate_plan(brand["posts_per_month"])
    posts = []

    for item in plan:
        hook = random.choice(HOOKS[item["post_type"]])
        prompt_data = {
            "brand_name": brand["brand_name"],
            "niche": brand["niche"],
            "audience": brand["audience"],
            "tone": brand["tone"],
            "post_type": item["post_type"],
            "angle": hook
        }

        prompt = build_prompt(template, prompt_data)
        content = generate_post(prompt)

        posts.append({
            "day": item["day"],
            "post_type": item["post_type"],
            "content": content
        })

    save_posts(posts, "output/posts.csv")


if __name__ == "__main__":
    main()
