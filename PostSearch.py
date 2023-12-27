def post_search(graph, keyword):
    matching_posts = []

    for user_id in graph.nodes:
        user_name = graph.nodes[user_id].get('name', 'unknown')
        user_posts = graph.nodes[user_id].get('posts', [])

        for post in user_posts:
            if post.find("body") is not None:
                post_body = post.find("body").value
            else:
                post_body = ""

            # Check if the keyword is present in the post body
            if keyword.lower() in post_body.lower():
                matching_posts.append((user_id, user_name, post_body))
                continue

            # Check if the keyword is present in any topic
            topics = post.find("topics")
            if topics is not None:
                for topic in topics.findall("topic"):
                    topic_text = topic.value
                    if keyword.lower() in topic_text.lower():
                        matching_posts.append((user_id, user_name, post_body))
                        break

    if not matching_posts:
        print(f"There is no post whose topic is '{keyword}' or contain the keyword '{keyword}'.")
    else:
        print(f"Posts whose topic is '{keyword}' or contain the word '{keyword}' in it:")
        for user_id, user_name, post_body in matching_posts:
            print(f"User ID: {user_id}, Name: {user_name}, Post: {post_body}\n")

    return matching_posts
