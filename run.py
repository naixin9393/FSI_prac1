# Search methods

import search


def test(from_city, to_city):
    ab = search.GPSProblem(from_city, to_city, search.romania)
    bfs_generated, bfs_visited, bfs_path, bfs_path_cost = search.breadth_first_graph_search(ab)
    dfs_generated, dfs_visited, dfs_path, dfs_path_cost = search.depth_first_graph_search(ab)
    bnb_generated, bnb_visited, bnb_path, bnb_path_cost = search.branch_and_bound_graph_search(ab)
    bnbh_generated, bnbh_visited, bnbh_path, bnbh_path_cost = search.branch_and_bound_heuristic_graph_search(ab)

    print("\nFrom", from_city, "to", to_city)
    print("BFS - generated =", bfs_generated, ", visited =", bfs_visited, ", path:", bfs_path, ", cost:", bfs_path_cost)
    print("DFS - generated =", dfs_generated, ", visited =", dfs_visited, ", path:", dfs_path, ", cost:", dfs_path_cost)
    print("BNB - generated =", bnb_generated, ", visited =", bnb_visited, ", path:", bnb_path, ", cost:", bnb_path_cost)
    print("BNBH - generated =", bnbh_generated, ", visited =", bnbh_visited, ", path:", bnbh_path, ", cost:", bnbh_path_cost)


test('A', 'B')
test('O', 'E')
test('G', 'Z')
test('N', 'D')
test('M', 'F')

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
