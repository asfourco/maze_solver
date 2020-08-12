from solver.vertex import Vertex
from solver.pattern import Pattern
from collections import deque
from typing import List, Tuple, Optional
from numpy import full


class Maze:
    def __init__(
        self, entry_char: str, wall_char: str, data: list, pattern: Pattern
    ) -> None:
        self.wall = wall_char
        self.entry = entry_char
        self.data = data  # store the raw input
        # Initialize an empty matrix
        self.matrix = full((len(data), len(data[0])), None)
        for row in range(len(data)):
            for col in range(len(data[0])):
                self.matrix[row][col] = Vertex(col=col, row=row, data=data[row][col])
        self.pattern = pattern
        self.path: deque = deque()

    def __str__(self) -> str:
        return "\n".join("".join(row) for row in self.data)

    def reset(self) -> None:
        for vertex in self.matrix.flatten():
            vertex.d = float("inf")
            vertex.processed = False
        self.pattern.index = 0

    def find_entry_points(self) -> List[Optional[Vertex]]:
        entry_points = []
        for i, line in enumerate(self.data):
            try:
                line.index(self.entry)
            except ValueError:
                continue
            else:
                entry_points.append(self.get((i, line.index(self.entry))))
        return entry_points

    def get(self, location: tuple) -> Optional[Vertex]:
        row, col = location
        try:
            data = self.matrix[row][col]
        except ValueError:
            return None
        else:
            return data

    @property
    def shape(self) -> Tuple[int, int]:
        return (len(self.matrix), len(self.matrix[0]))

    def getNodeOnLeft(self, node: Vertex) -> Optional[Vertex]:
        neighbour = self.get((node.row, node.col - 1))
        if neighbour and not neighbour.processed:
            return neighbour
        else:
            return None

    def getNodeOnRight(self, node: Vertex) -> Optional[Vertex]:
        neighbour = self.get((node.row, node.col + 1))
        if neighbour and not neighbour.processed:
            return neighbour
        else:
            return None

    def getNodeAbove(self, node: Vertex) -> Optional[Vertex]:
        neighbour = self.get((node.row - 1, node.col))
        if neighbour and not neighbour.processed:
            return neighbour
        else:
            return None

    def getNodeBelow(self, node: Vertex) -> Optional[Vertex]:
        neighbour = self.get((node.row + 1, node.col))
        if neighbour and not neighbour.processed:
            return neighbour
        else:
            return None

    def get_neighbours(self, node: Vertex) -> List[Optional[Tuple[Vertex, float]]]:
        neighbours = {
            "above": self.getNodeAbove(node),
            "below": self.getNodeBelow(node),
            "left": self.getNodeOnLeft(node),
            "right": self.getNodeOnRight(node),
        }
        return [
            (node, self.get_distance(node, self.pattern.expected_step))
            for node in neighbours.values()
            if node
        ]

    def get_distance(self, target: Vertex, expected: str) -> float:
        distance = float("inf")  # default value
        # If we have a valid neighbour then the distance is one
        if target.data != self.wall and (
            target.data == expected or target.data == self.entry
        ):
            distance = 1
        return distance

    def find_path(self, source: Vertex, destination: Vertex) -> Tuple[bool, str]:
        # reset the maze matrix if we already have a result
        if len(self.path) > 0:
            self.reset()

        current_node = source
        current_node.d = 0
        while current_node:
            valid_node = None
            for node, dist in self.get_neighbours(current_node):
                # Find the first valid neighbour
                if current_node.d + dist < node.d:
                    node.d = current_node.d + dist
                    node.parent = current_node
                    valid_node = node
                    break
            current_node.processed = True

            # Check if we have a valid path forward, if not, go back a step
            if valid_node:
                current_node = valid_node
                self.pattern.next_step()
                # Break out of the while loop because we reached the end
                if valid_node.data == self.entry:
                    break
            else:
                # trace back to previous node and look for valid neighbours
                current_node = current_node.parent
                self.pattern.previous_step()

        if not current_node:
            return False, "No Path found!"

        while current_node:
            self.path.appendleft(current_node)
            current_node = current_node.parent if current_node.parent else None

        return True, f"Path Found of length: {self.path[-1].d}"

    def generate_output(self, path: deque = None) -> list:
        matrix = full((len(self.data), len(self.data[0])), "_")
        if not path:
            path = self.path
        for entry in path:
            matrix[entry.row][entry.col] = entry.data
        return matrix
