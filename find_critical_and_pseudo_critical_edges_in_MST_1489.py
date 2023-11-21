from collections import defaultdict
from typing import List, Set, Dict

Edge = List[int]
Graph = List[Edge]
MST = Graph


class Solution:
    @staticmethod
    def findCriticalAndPseudoCriticalEdges(n: int, edges: Graph) -> List[List[int]]:
        orig_edge_i_by_edge_hash: Dict[str, int] = {
            f"{edge[0]}-{edge[1]}-{edge[2]}": edge_i
            for edge_i, edge in enumerate(edges)
        }
        edges.sort(key=lambda edge: edge[2])
        min_mst_cost = Solution.get_MST_cost(n, edges, -1, -1)

        unique_weights = Solution.get_unique_weights(edges)

        # find all critical edges
        critical_edge_is: Set[int] = set()
        for skip_edge_i in range(len(edges)):
            mst_cost = Solution.get_MST_cost(n, edges, skip_edge_i, -1)
            if mst_cost != min_mst_cost:
                critical_edge = edges[skip_edge_i]
                edge_hash = f"{critical_edge[0]}-{critical_edge[1]}-{critical_edge[2]}"
                critical_edge_is.add(orig_edge_i_by_edge_hash[edge_hash])

        # find all non-critical edges
        pseudo_critical_edge_is: List[int] = []
        for force_edge_i in range(len(edges)):
            forced_edge = edges[force_edge_i]
            if forced_edge[2] in unique_weights:
                continue
            forced_edge_hash = f"{forced_edge[0]}-{forced_edge[1]}-{forced_edge[2]}"
            orig_edge_i = orig_edge_i_by_edge_hash[forced_edge_hash]

            if orig_edge_i in critical_edge_is:
                continue

            mst_cost = Solution.get_MST_cost(n, edges, -1, force_edge_i)
            if mst_cost == min_mst_cost:
                pseudo_critical_edge_is.append(orig_edge_i)

        return [list(critical_edge_is), pseudo_critical_edge_is]

    @staticmethod
    def get_MST_cost(n: int, edges: Graph, skip_edge_i: int, force_edge_i: int) -> int:
        acc_cost = 0
        group_by_v = [i for i in range(n)]
        vs_by_group = [[i] for i in range(n)]
        if force_edge_i > -1:
            forced_v1, forced_v2, forced_edge_weight = edges[force_edge_i]
            group_by_v[forced_v1] = forced_v2
            vs_by_group[forced_v2] += vs_by_group[forced_v1]
            vs_by_group[forced_v1] = []
            acc_cost += forced_edge_weight
        for edge_i in range(len(edges)):
            if edge_i == skip_edge_i or edge_i == force_edge_i:
                continue
            v1, v2, edge_weight = edges[edge_i]
            v1_group = group_by_v[v1]
            v2_group = group_by_v[v2]
            if v1_group == v2_group:
                continue
            acc_cost += edge_weight
            for v in vs_by_group[v1_group]:
                group_by_v[v] = group_by_v[v2]
            vs_by_group[v2_group] += vs_by_group[v1_group]
            vs_by_group[v1_group] = []
            if len(vs_by_group[v2_group]) == n:
                return acc_cost
        return 1000000000000

    @staticmethod
    def get_unique_weights(edges: Graph) -> Set[int]:
        repetitions_by_weight: Dict[int, int] = defaultdict(lambda: 0)
        for _, _, weight in edges:
            repetitions_by_weight[weight] += 1
        unique_weights: Set[int] = set()
        for weight in repetitions_by_weight:
            reps = repetitions_by_weight[weight]
            if reps == 1:
                unique_weights.add(weight)
        return unique_weights


def test_find_critical_and_pseudo_critical_edges():
    output = Solution.findCriticalAndPseudoCriticalEdges(
        5, [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]
    )
    assert output == [[0, 1], [2, 3, 4, 5]]

    output = Solution.findCriticalAndPseudoCriticalEdges(
        4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]
    )
    assert output == [[], [0, 1, 2, 3]]

    output = Solution.findCriticalAndPseudoCriticalEdges(
        6, [[0, 1, 1], [1, 2, 1], [0, 2, 1], [2, 3, 4], [3, 4, 2], [3, 5, 2], [4, 5, 2]]
    )
    assert output == [[3], [0, 1, 2, 4, 5, 6]]

    output = Solution.findCriticalAndPseudoCriticalEdges(
        4, [[0, 1, 1], [0, 3, 1], [0, 2, 1], [1, 2, 1], [1, 3, 1], [2, 3, 1]]
    )
    assert output == [[], [0, 1, 2, 3, 4, 5]]


if __name__ == "__main__":
    test_find_critical_and_pseudo_critical_edges()
