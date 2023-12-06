def post_search(graph, keyword):
    matching_posts = []

    for user_id in graph.nodes:
        user_posts = graph.nodes[user_id].get('posts', [])
        for post in user_posts:
            if keyword.lower() in post.lower():
                matching_posts.append((user_id, post))

    if not matching_posts:
        print(f"No posts found containing the keyword '{keyword}'.")
    else:
        print(f"Posts containing the keyword '{keyword}':")
        for user_id, post in matching_posts:
            print(f"User ID {user_id}: {post}\n")

    return matching_posts
