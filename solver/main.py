from solver.vertex import Vertex
from solver.pattern import Pattern
from collections import deque
from typing import List, Tuple, Optional
import numpy as np


class Maze:
    def __init__(
        self, entry_char: str, wall_char: str, data: list, pattern: Pattern
    ) -> None:
        self.wall = wall_char
        self.entry = entry_char
        self.data = data
        # Initialize an empty matrix
        self.matrix = np.full((len(data), len(data[0])), None)
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

        if len(self.path) > 0:
            return True, f"Path Found of length: {len(self.path)}"

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

        return True, f"Path Found of length: {len(self.path)}"

    def generate_output(self, path: deque = None) -> list:
        matrix = np.full((len(self.data), len(self.data[0])), "_")
        if not path:
            path = self.path
        for entry in path:
            matrix[entry.row][entry.col] = entry.data
        return matrix


def read_input(path: str) -> list:
    with open(path, "r") as file:
        data = file.read()
    return data.split("\n")


def write_output(data: list, path: str) -> None:
    with open(path, "w") as file:
        for line in data:
            file.write(f"{''.join(line)}\n")


def run(input_path: str, output_path: str) -> None:
    input = read_input(input_path)
    entry_char = input[0]
    wall_char = input[1]
    pattern = Pattern(input[2])
    map_data = input[3:]
    maze = Maze(
        entry_char=entry_char, wall_char=wall_char, data=map_data, pattern=pattern
    )

    try:
        source, destination = maze.find_entry_points()
    except ValueError:
        print("Maze has no entry/exit points")
        return

    print(
        f"Finding path in maze shape of (rows, cols):{maze.shape}, using path pattern: '{pattern}' ..."
    )
    success, msg = maze.find_path(source=source, destination=destination)
    print(msg)

    if success:
        map_data = maze.generate_output()
        write_output(data=map_data, path=output_path)

        for line in map_data:
            print(f"{''.join(line)}")

        print(f"Results written to {output_path}")
