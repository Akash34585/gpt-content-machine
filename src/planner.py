def generate_plan(total_posts: int):
    post_types = ["educational", "insight", "mistake", "tip"]
    plan = []

    for i in range(total_posts):
        plan.append({
            "day": i + 1,
            "post_type": post_types[i % len(post_types)]
        })

    return plan
