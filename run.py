# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
bfs_generated, bfs_visited, bfs_path = search.breadth_first_graph_search(ab)
dfs_generated, dfs_visited, dfs_path = search.depth_first_graph_search(ab)
bnb_generated, bnb_visited, bnb_path = search.branch_and_bound_graph_search(ab)

print("BFS - generated =", bfs_generated, ", visited =", bfs_visited, ", path:", bfs_path)
print("DFS - generated =", dfs_generated, ", visited =", dfs_visited, ", path:", dfs_path)
print("BNB - generated =", bnb_generated, ", visited =", bnb_visited, ", path:", bnb_path)

# print(search.breadth_first_graph_search(ab).path())
# print(search.depth_first_graph_search(ab).path())
# print(search.branch_and_bound_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
