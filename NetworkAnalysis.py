# 1. Most Influential Users (Most Followers)
# 1. Most Influential Users (Most Followers)
def most_influential(graph):
    user_ids = []
    out_degrees = []

    for user in graph.nodes:
        user_ids.append(user.id)
        out_degrees.append(len(graph.successors(user.id)))

    max_out_degree = max(out_degrees)

    most_influential_users = [user_ids[i] for i, degree in enumerate(out_degrees) if degree == max_out_degree]

    print(f"The most influential users are: {most_influential_users}")
    return most_influential_users


# 2. Most Active User (Connected to Lots of Users)
def most_active(graph):
    user_ids = []
    total_edges = []

    for user in graph.nodes:
        user_ids.append(user.id)
        total_edges.append(graph.degree(user.id))

    max_total_edges = max(total_edges)

    most_active_users = [user_ids[i] for i, degree in enumerate(total_edges) if degree == max_total_edges]

    print(f"The most active users are: {most_active_users}")
    return most_active_users


# 3.  Mutual followers between 2 users
def mutual_followers(graph, node1_id, node2_id):
    node1 = graph.find_node(str(node1_id))
    node2 = graph.find_node(str(node2_id))

    if not node1 or not node2:
        print("Invalid nodes. Please provide existing nodes.")
        return None

    followers_node1 = [successor.id for successor in graph.successors(str(node1_id))]
    followers_node2 = [successor.id for successor in graph.successors(str(node2_id))]

    mut_followers = [follower for follower in followers_node1 if follower in followers_node2]
    print(f"Mutual followers between nodes {node1_id} and {node2_id}: {mut_followers}")
    return mut_followers


# 4.  Suggest users to follow
def suggest_followers(graph):
    suggested_followers = []

    for user in graph.nodes:
        user_suggestions = []

        for successor in graph.successors(user.id):
            for suggested_follower in graph.successors(successor.id):
                if suggested_follower not in graph.predecessors(user.id) and suggested_follower.id != user.id and suggested_follower.id not in user_suggestions:
                    user_suggestions.append(suggested_follower.id)

        suggested_followers.append((user.id, user_suggestions))

    for user, user_suggestions in suggested_followers:
        print(f"Suggested followers for User {user}: {user_suggestions}")

    return suggested_followers