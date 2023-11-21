from dataclasses import dataclass
from heapq import heappush, heappop
from typing import List, Tuple, Optional, Dict


@dataclass
class QuadTreeNode:
    point: (int, int)
    top_left_node: Optional["QuadTreeNode"]
    top_right_node: Optional["QuadTreeNode"]
    bottom_left_node: Optional["QuadTreeNode"]
    bottom_right_node: Optional["QuadTreeNode"]


def manhatten_distance(p1: List[int], p2: List[int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


class Solution:
    @staticmethod
    def minCostConnectPoints(points: List[List[int]]) -> int:
        # using kruskal's algorithm
        acc_cost = 0
        edges: List[(int, int, int)] = []
        for src_point_i in range(len(points)):
            for dest_point_i in range(src_point_i + 1, len(points)):
                src_point = points[src_point_i]
                dest_point = points[dest_point_i]
                heappush(edges, (manhatten_distance(src_point, dest_point), src_point_i, dest_point_i))

        group_by_point_i = [i for i in range(len(points))]
        point_is_by_group = [[i] for i in range(len(points))]
        while len(edges):
            edge_len, point_a_i, point_b_i = heappop(edges)
            point_a_group = group_by_point_i[point_a_i]
            point_b_group = group_by_point_i[point_b_i]
            if point_a_group == point_b_group:
                continue
            acc_cost += edge_len
            for point_i in point_is_by_group[point_a_group]:
                group_by_point_i[point_i] = group_by_point_i[point_b_i]
            point_is_by_group[point_b_group] += point_is_by_group[point_a_group]
            point_is_by_group[point_a_group] = []
        return acc_cost

    # @staticmethod
    # def minCostConnectPoints(points: List[List[int]]) -> int:
    #     point_idxs_by_group_idx: Dict[List[int]] = {i: [i] for i in range(len(points))}
    #     acc_cost = 0
    #     loop_guard = 0
    #     while len(point_idxs_by_group_idx) > 1:
    #         loop_guard += 1
    #         if loop_guard > 1000000000:
    #             raise Exception("unterminated while loop")
    #         group_idx_to_connect = list(point_idxs_by_group_idx.keys())[0]
    #         min_cost = 1000000000
    #         min_cost_group_idx = -1
    #         for group_idx, point_idxs in point_idxs_by_group_idx.items():
    #             if group_idx == group_idx_to_connect:
    #                 continue
    #             for dest_point_idx in point_idxs:
    #                 for src_point_idx in point_idxs_by_group_idx[group_idx_to_connect]:
    #                     dest_point = points[dest_point_idx]
    #                     src_point_idx = points[src_point_idx]
    #                     cost = abs(src_point_idx[0] - dest_point[0]) + abs(src_point_idx[1] - dest_point[1])
    #                     assert cost != 0
    #                     if cost < min_cost:
    #                         min_cost = cost
    #                         min_cost_group_idx = group_idx
    #         acc_cost += min_cost
    #         point_idxs_by_group_idx[min_cost_group_idx] += point_idxs_by_group_idx[group_idx_to_connect]
    #         del point_idxs_by_group_idx[group_idx_to_connect]
    #     return acc_cost

    # for point_idx, point in enumerate(points):
    #     min_cost_dest_idx = -1
    #     min_cost = 10000000
    #     for dest_idx, dest in enumerate(points):
    #         cost = abs(point[0] - dest[0]) + abs(point[1] - dest[1])
    #         if cost == 0:
    #             continue
    #         if cost < min_cost:
    #             min_cost = cost
    #             min_cost_dest_idx = dest_idx
    #     point_idxs_by_line_idx.append((point_idx, min_cost_dest_idx))
    #
    #     if min_cost_dest_idx

    @staticmethod
    def quad_from_points(points: List[List[int]]) -> Optional[QuadTreeNode]:
        if not points:
            return None
        if len(points) > 1:
            x_sorted_points = sorted(points, key=lambda point: point[0])
            mid_idx = len(points) // 2
            left_y_sorted_points = sorted(x_sorted_points[:mid_idx], key=lambda point: point[1])
            right_y_sorted_points = sorted(x_sorted_points[mid_idx:], key=lambda point: point[1])
            left_points_mid_idx = len(left_y_sorted_points) // 2
            right_points_mid_idx = len(right_y_sorted_points) // 2
            top_left_points = left_y_sorted_points[:left_points_mid_idx]
            top_right_points = right_y_sorted_points[:right_points_mid_idx]
            bottom_left_points = left_y_sorted_points[left_points_mid_idx:]
            bottom_right_points = right_y_sorted_points[left_points_mid_idx:]
            top_left_node = Solution.quad_from_points(top_left_points)
            top_right_node = Solution.quad_from_points(top_right_points)
            bottom_left_node = Solution.quad_from_points(bottom_left_points)
            bottom_right_node = Solution.quad_from_points(bottom_right_points)
            # QuadTreeNode(point=, top_left_node=top_left_node, top_right_node=top_right_node,
            #              bottom_left_node=bottom_left_node, bottom_right_node=bottom_right_node)


def test_min_cost_connect_points():
    assert Solution.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20
