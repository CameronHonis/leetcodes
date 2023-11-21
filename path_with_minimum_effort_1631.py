from dataclasses import dataclass
from heapq import heappush, heappop, heapify
from typing import List, Dict

CoordsStr = str
DEBUG = True


@dataclass
class UnvisitedNode:
    r: int
    c: int
    prev_r: int
    prev_c: int
    g_score: int
    h_score: float
    visited: bool = False

    def __lt__(self, other: "UnvisitedNode"):
        self_f_score = self.g_score + self.h_score
        other_f_score = other.g_score + other.h_score
        return self_f_score < other_f_score

    def __gt__(self, other: "UnvisitedNode"):
        self_f_score = self.g_score + self.h_score
        other_f_score = other.g_score + other.h_score
        return self_f_score > other_f_score

    def __repr__(self):
        return f"<{self.r}, {self.c}>({self.g_score})"


class Solution:
    @staticmethod
    def h_score(r: int, c: int, heights: List[List[int]]) -> float:
        # can't use any heuristic related to effort since the max effort along the path is the only metric that
        # determines path cost, and would require a full graph traversal to calculate precisely. Estimates cannot
        # be tuned to be solely optimistic (they can, but it would significantly degrade the usefulness of the
        # heuristic). So instead, we use a heuristic-less dijkstra search algorithm.
        return 0.
        # dist = abs(len(heights) - 1 - r) + abs(len(heights[0]) - 1 - c)
        # if dist == 0:
        #     return 0
        # height_diff = abs(heights[-1][-1] - heights[r][c])
        # return height_diff / dist

    @staticmethod
    def initialize_discovered_nodes(heights: List[List[int]]) -> Dict[CoordsStr, UnvisitedNode]:
        rtn: Dict[CoordsStr, UnvisitedNode] = {
            "0 0": UnvisitedNode(0, 0, prev_r=-1, prev_c=-1, g_score=0, h_score=-1, visited=True),
        }
        origin_height = heights[0][0]
        if len(heights) > 1:
            node_below_g_score = abs(origin_height - heights[1][0])
            node_below_h_score = Solution.h_score(1, 0, heights)
            rtn["1 0"] = UnvisitedNode(1, 0, prev_r=0, prev_c=0, g_score=node_below_g_score, h_score=node_below_h_score)
        if len(heights[0]) > 1:
            node_right_h_score = Solution.h_score(0, 1, heights)
            node_right_g_score = abs(origin_height - heights[0][1])
            rtn["0 1"] = UnvisitedNode(0, 1, prev_r=0, prev_c=0, g_score=node_right_g_score, h_score=node_right_h_score)
        return rtn

    @staticmethod
    def minimumEffortPath(heights: List[List[int]]) -> int:
        if len(heights) == 1 and len(heights[0]) == 1:
            return 0
        discovered_nodes: Dict[CoordsStr, UnvisitedNode] = Solution.initialize_discovered_nodes(heights)
        boundary_nodes_queue: List[UnvisitedNode] = []
        if "1 0" in discovered_nodes:
            heappush(boundary_nodes_queue, discovered_nodes["1 0"])
        if "0 1" in discovered_nodes:
            heappush(boundary_nodes_queue, discovered_nodes["0 1"])
        g_scores_by_coords = []
        if DEBUG:
            g_scores_by_coords = [[-1] * len(heights[0]) for _ in range(len(heights))]
        while True:
            if DEBUG:
                print(boundary_nodes_queue)
            node_to_explore = heappop(boundary_nodes_queue)
            node_to_explore.visited = True
            r = node_to_explore.r
            c = node_to_explore.c
            if DEBUG:
                g_scores_by_coords[r][c] = node_to_explore.g_score
            if r == len(heights) - 1 and c == len(heights[0]) - 1:
                # found optimal path to goal
                return node_to_explore.g_score
            for r_incr, c_incr in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_r = node_to_explore.r + r_incr
                new_c = node_to_explore.c + c_incr
                if new_r < 0 or new_r >= len(heights) or new_c < 0 or new_c >= len(heights[0]):
                    continue
                node_to_discover_hash = f"{new_r} {new_c}"
                effort = abs(heights[r][c] - heights[new_r][new_c])
                discovered_g_score = max(node_to_explore.g_score, effort)
                discovered_h_score = Solution.h_score(new_r, new_c, heights)
                if node_to_discover_hash not in discovered_nodes:
                    node_to_discover = UnvisitedNode(r=new_r, c=new_c, prev_r=r, prev_c=c, g_score=discovered_g_score,
                                                     h_score=discovered_h_score, visited=False)
                    discovered_nodes[node_to_discover_hash] = node_to_discover
                    heappush(boundary_nodes_queue, node_to_discover)
                elif discovered_nodes[node_to_discover_hash].g_score > discovered_g_score:
                    node_to_discover = discovered_nodes[node_to_discover_hash]
                    if node_to_discover.visited:
                        continue
                    node_to_discover.g_score = discovered_g_score
                    node_to_discover.prev_r = r
                    node_to_discover.prev_c = c
                    heapify(boundary_nodes_queue)


def test_minimum_effort_path():
    assert Solution.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2
    assert Solution.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]) == 1
    assert Solution.minimumEffortPath(
        [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]) == 0
    assert Solution.minimumEffortPath([[3]]) == 0
    assert Solution.minimumEffortPath([[1, 2, 4, 3]]) == 2
